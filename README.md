# Jureg Dice Roll
Telegram bot to roll dices.

## Settings

Rename the sample.secrets.toml file to .secrets.toml

```
mv sample.secrets.toml .secrets.toml
```
Fill the variable if their actual values: Eg:

```
TOKEN="r328490328948390890fewrewfdsf039"
```

## Run

```
docker-compose up
```
or run as daemon

```
docker-compose up -d
```

## Commands
	/dicemenu => Create a menu with the most common dice types: d4, d6, d8, d10, d12, d20 and d100.
	/d100 => Roll the most common used dice for this bot.
	*d#n#* => where #n# is a number of the dice that should be rolled.
