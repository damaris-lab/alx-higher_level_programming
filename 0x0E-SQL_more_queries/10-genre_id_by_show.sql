--  lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT subquery.id, subquery.title, tv_show_genres.genre_id
FROM (
    SELECT tv_shows.id, tv_shows.title
    FROM tv_shows
    WHERE tv_shows.id IN (
        SELECT tv_show_genres.tv_show_id
        FROM tv_show_genres
    )
) AS subquery
JOIN tv_show_genres ON subquery.id = tv_show_genres.tv_show_id
ORDER BY subquery.title ASC, tv_show_genres.genre_id ASC;

