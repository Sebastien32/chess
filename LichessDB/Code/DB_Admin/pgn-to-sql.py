# Copyright (c) 2017, balping
# https://github.com/balping 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pgn
import sys
import datetime
# Declare fields to be searched
fields = 	['event', 'site', 'white', 'black', 'result', 'utcdate', 'utctime', 
			'whiteelo', 'blackelo', 'whiteratingdiff', 'blackratingdiff', 'eco',
			'opening', 'timecontrol', 'termination'];

def values_row (game):
	ret = '('
	for field in fields:
		if hasattr(game, field):
			ret += ' \'' + getattr(game, field).replace('\'', '\'\'') + '\', '
		else:
			# Add '' (empty strin)
			ret += ' \'\', '

	if hasattr(game, 'moves'):
		ret += str(len(game.moves)) + ', '
		ret += ' \'' + ' '.join(game.moves) + '\''
	else:
		ret += '0, \'\''

	ret += ')'
	return ret
# If the user didn't input two command-line arguments
if len(sys.argv) != 2:
	# Print an error message
	print 'Usage: python pgn-to-sql.py input.pgn > out.sql'
# Start an SQLITE transaction
print 'BEGIN;'
# Set i, an increment counter to 0
i = 0
# For every game in the pgn
for game in pgn.GameIterator(sys.argv[1]):
	# If the game doesn't have a result
	if not(hasattr(game, 'result')):
		# End the loop
		break;
	# If the game is a multiple of 500
	if (i % 500) == 0:
		# Print out an insert clause
		print 'INSERT INTO "2016-11"' + ' VALUES '
	# If this is the last game in this insert statement
	if (i % 500) == 499:
		# Print a semicolon to end the insert statement
		print values_row(game), ';'
	# If this is not the last game in this insert statement
	else:
		# Print a comma to continue the insert statement
		print values_row(game), ','
	# Increment the counter variable
	i += 1
	# If the increment counter is a multiple of 10,000
	if (i % 10000) == 0:
		# Display the progress of the process to the terminal along with a timestamp
		sys.stderr.write("Completed " + str(i) + " entries at " + str(datetime.datetime.now()) + "\n")
# If the increment counter is not 0
if (i % 500) < 499:
	# Fix the trailing comma problem by inserting a null row
	print '(NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)'
# Print a semicolon to end the last insert statement
print ';'
# Delete the null row from the bottom of the table
print 'DELETE FROM "2016-11" WHERE rowid = last_insert_rowid();'
# End the SQLite transaction
print 'COMMIT;'