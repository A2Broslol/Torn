module.exports = class Planet {
	constructor(i, name) {
		this.type = "Planet",
		this.name = name,
		this.color = "yellow",
		this.owner = 0, // string name of the player who owns it.
		this.id = i, // unique identifier
		this.x = sectorWidth / 2, // this is updated by the createPlanet function to a random location
		this.y = sectorWidth / 2,
		this.cooldown = 0, // to prevent chat "planet claimed" spam
		this.sx = 0,
		this.sy = 0;
	}
	
	tick() {
		this.cooldown--;
		if (tick % 12 == 6 && this.owner != 0) for (var i in players[this.sy][this.sx]) {
			var p = players[this.sy][this.sx][i];
			if (this.owner === p.name) p.money++; // give money to owner
		}
	}
};