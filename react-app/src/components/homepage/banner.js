import React, { useEffect, useState } from 'react';
import axios from 'axios';
import bannerImage from './bannerwa1.png';
const Banner = () => {
    const [championImage, setChampionImage] = useState(null);

    useEffect(() => {
        const fetchRandomChampion = async () => {
            try {
                const response = await axios.get('https://ddragon.leagueoflegends.com/cdn/10.16.1/data/en_US/champion.json');
                const championKeys = Object.keys(response.data.data);
                const randomChampionKey = championKeys[Math.floor(Math.random() * championKeys.length)];
                const championSplashArt = `http://ddragon.leagueoflegends.com/cdn/img/champion/splash/${randomChampionKey}_0.jpg`;

                setChampionImage(championSplashArt);
            } catch (error) {
                console.error(error);
            }
        };
        fetchRandomChampion();
    }, []);

    return (
        <div
            className="banner"
            style={{ backgroundImage: `url(${championImage})`,
            backgroundSize: "cover",
            backgroundPosition: "center top",
            backgroundRepeat: "no-repeat",
            
                    }}

        >
            <img src={bannerImage} alt="Banner" />
            <div style={{
                position: "absolute",
                width: "508px",
                height: "104px",
                left: "112px",
                top: "20%",
                fontFamily: "'Montserrat', sans-serif",
                fontStyle: "normal",
                fontWeight: "700",
                fontSize: "96px",
                lineHeight: "104px",
                letterSpacing: "-0.015em",
                color: "black"
            }}>
                COMPARE
            </div>

            <div style={{
                position: "absolute",
                width: "858px",
                height: "56px",
                left: "112px",
                top: "31%",
                fontFamily: "'Montserrat', sans-serif",
                fontStyle: "italic",
                fontWeight: "100",
                fontSize: "48px",
                lineHeight: "56px",
                color: "black"
            }}>
                Against the best players in the world
            </div>
            <button style={{
                display: "flex",
                flexDirection: "row",
                alignItems: "center",
                justifyContent: "space-between",
                padding: "16px 24px",
                position: "absolute",
                width: "169px",
                height: "52px",
                left: "112px",
                top: "45%",
                background: "#58B25D",
                boxShadow: "0px 6px 10px rgba(0, 0, 0, 0.14), 0px 1px 18px rgba(0, 0, 0, 0.12), 0px 3px 5px rgba(0, 0, 0, 0.2), inset 0px 4px 8px rgba(225, 248, 253, 0.1)",
                borderRadius: "8px",
                border: "none",
                color: "#FFFFFF",
                fontFamily: "'Montserrat', sans-serif",
                fontSize: "14px",
                fontWeight: "700",
                lineHeight: "20px",
                letterSpacing: "0.0125em",
                cursor: "pointer"
            }}>
                CHECK IT OUT
                <i className="fas fa-arrow-right"></i>
            </button>
        </div>
    );
};

export default Banner;
