<?php

// Code by toxic1835 (-TOXIC-)
// if you dont know what to do write me AND ONLY CHANGE "CHANGE!" STRINGS
// Keep in mind: ";" ARE EVERYTHING if you forget one, your site will die xD

function discordCallback() {
    $tokenUrl = 'https://discord.com/api/v10/oauth2/token';
    
    $clientId = 'YOUR_CLIENT_ID';                           // CHANGE!
    $clientSecret = 'YOUR_CLIENT_SECRET';                   // CHANGE!

    $redirectUri = 'https://IP_OR_DOMAIN/callback.php';     // CHANGE!
    
    if (isset($_GET['code'])) {
        $authorizationCode = $_GET['code'];
        
        $postData = array(
            'client_id' => $clientId,
            'client_secret' => $clientSecret,
            'grant_type' => 'authorization_code',
            'code' => $authorizationCode,
            'redirect_uri' => $redirectUri,
            'scope' => 'identify connections'
        );
        
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $tokenUrl);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $response = curl_exec($ch);
        curl_close($ch);
        
        $accessTokenData = json_decode($response, true);
        
        if (isset($accessTokenData['access_token'])) {
            $accessToken = $accessTokenData['access_token'];
            
            $userUrl = 'https://discord.com/api/v10/users/@me';
            $ch = curl_init();
            curl_setopt($ch, CURLOPT_URL, $userUrl);
            curl_setopt($ch, CURLOPT_HTTPHEADER, array('Authorization: Bearer ' . $accessToken));
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            $userInfo = curl_exec($ch);
            curl_close($ch);
            
            $connectionsUrl = 'https://discord.com/api/v10/users/@me/connections';
            $ch = curl_init();
            curl_setopt($ch, CURLOPT_URL, $connectionsUrl);
            curl_setopt($ch, CURLOPT_HTTPHEADER, array('Authorization: Bearer ' . $accessToken));
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            $connectionsInfo = curl_exec($ch);
            curl_close($ch);
            $steamidFound = false;
            
            $connectionsData = json_decode($connectionsInfo, true);
            foreach ($connectionsData as $connection) {
                if ($connection['type'] === 'steam') {
                    echo 'SteamID: ' . $connection['id'];
                    $steamidFound = true;
                }
            }
            if (!$steamidFound) {
                echo 'The system couldn\'t find steam in your profile connections!';
            }
        } else {
            echo 'There was an error getting you discord account.';
        }
    } else {
        echo 'No Authentification-Code set!';
    }
}

discordCallback();
?>
