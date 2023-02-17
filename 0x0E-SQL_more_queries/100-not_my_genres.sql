-- This script uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
AND tv_show_genres.show_id =
			(SELECT tv_shows.id
				FROM tv_shows
				WHERE tv_shows.title = 'Dexter')
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_genres.name ASC;
