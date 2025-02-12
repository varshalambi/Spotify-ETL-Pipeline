SELECT artist_id, track_name FROM warehouse
WHERE genre = "LoFi"
GROUP BY artist_id
ORDER BY streams DESC;
