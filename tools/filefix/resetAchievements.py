"""
Copyright (C) 2021  torn.space (https://torn.space)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

######################################
# Torn "FileFix" 4
# Date: 07/03/2021
# Purpose: Reset all players' achievements
#####################################

MONGO_CONNECTION_STR = "mongodb://localhost:27017/torn"
from pymongo import MongoClient

print("*** RUNNING TORN FILEFIX 4: RESETTING ACHIEVEMENTS ***")
client = MongoClient(MONGO_CONNECTION_STR)
db = client.torn
players = db.players

for player in players.find():
    print(f"Processing: {player['_id']}")

    players.update_one({"_id": player["_id"]}, {"$unset": {"killsAchs": 0, "moneyAchs": 0, "driftAchs": 0, "randmAchs": 0}})
