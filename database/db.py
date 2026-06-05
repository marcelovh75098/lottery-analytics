def insert_test_draw():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    try:

        cursor.execute("""
        INSERT INTO baloto_draws
        (
            draw_date,
            n1,
            n2,
            n3,
            n4,
            n5,
            superbalota
        )
        VALUES
        (
            '2026-01-01',
            1,
            2,
            3,
            4,
            5,
            6
        )
        """)

        conn.commit()

    except:
        pass

    conn.close()

