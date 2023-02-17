-- This script lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
AND tv_show_genres.genre_id =
			(SELECT tv_genres.id
				FROM tv_genres
				WHERE tv_genres.name = 'Comedy')
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title ASC;
