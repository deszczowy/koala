# Koala
`version 0.5`

> There are nine million todo apps on GitHub\
> That's a fact\
> It's a thing we can't deny\
> Like the fact that I will make another one

This app born of frustration that there is no simple todo application for me out there. Most of them are packed with features which i don't need, or have no both Windows and Linux clients, or their clients are RAM consuming Electron wraps, or are discontinued on recent distros, or something else, you name it. 

So, this one is for me.

## Cookbook

### *Add* ([&#10010;](https://unicode-table.com/en/271A/), `Ctrl+N`)
Use it to add new task to the tree. If you want to add subtask to existing task, select this task before clicking.

### *Edit* ([&#0177;](https://unicode-table.com/en/00B1/), `Ctrl+E`)
Select task you want to edit and click this button. You will see a "new task" form filled with task data.

`Ctrl+Q` - confirms adding or editing the task\
`Esc` - cancels process

### *Delete* ([&#10005;](https://unicode-table.com/en/2715/), `Ctrl+D`)
Use it to remove selected task, but remember, if any of subtasks are not done, removing will fail.

### *Recycle* ([&#11119;](https://unicode-table.com/en/2B6F/), `Ctrl+R`)
Many done tasks on a list? Throw them all away at once with this special button.

### *Casette* ([&#128429;](https://unicode-table.com/en/1F5AD/), `Ctrl+B`)
Use it to store current state of the tree in a snapshot file.

## Hints

- Items can be deselect by clicking on the free space below the tree (status bar included).
- Double click on task to unfold description.

## Autosave

Task saves automatic every 7 second and when closing. But who would close such a great app?

## Storage and syncing

Tasks are stored in plain text file. You can manage your cloud syncing by pointing the app to your synced catalog. In order to do this, open or create `config.txt` file next to executable and put there an absolute path to your catalog (this file was created only for this). You can define plenty of paths there, app will go with first one that happen to exists. If you leave this file empty or path is invalid, or `config.txt` not exist - app will store task in file next to executable. There is no need to restart an app, because every change done outside will refresh the tree.

Backup tapes will be stored in `tapes` directory in provided path.

You don't even need app to add or remove tasks since they are stored in plain text file. It could by painful, but not impossible. Look around, if you want. Little tip here: row identifiers does not have to be uuids, any reasonable string will work. Storage file is utf-8 encoded.

## Categories, anyone?

Too long todo list is pointless. How many categories for your tasks do you need? Just keep your list short and organize your tasks in tree. Trust me, you will not need categories. 

## Warranty

This project is MIT licensed, the SOFTWARE is provided "AS IS", WITHOUT WARRANTY OF ANY KIND, so yeah, do backups!

## Credits

Beautiful icon was made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>.

## Work in progress

It is not polished piece of art, need some work maybe. Some highlights of what has to be done are pointed below:

- reminders list 
- reminder window or system notification

More extensive todo list is stored in, well, this app :)

## Plans

Main focus now is on fixing bugs and ease of using. The only planned feature is reminder trigger, but I will think about it. Thats it. This is simple todo list. No calendars, no Markdown or picture support, no additional notes, no internet connection with fridge.