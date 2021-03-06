<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
    <link rel="stylesheet" href="https://unpkg.com/purecss@1.0.0/build/pure-min.css"
          integrity="sha384-nn4HPE8lTHyVtfCBi5yW9d20FjT8BJwUXyWZT9InLYax14RDjBj46LmSztkmNP9w" crossorigin="anonymous">
    <!--[if lte IE 8]>
    <link rel="stylesheet" href="https://unpkg.com/purecss@1.0.0/build/grids-responsive-old-ie-min.css">
    <![endif]-->
    <!--[if gt IE 8]><!-->
    <link rel="stylesheet" href="https://unpkg.com/purecss@1.0.0/build/grids-responsive-min.css">
    <!--<![endif]-->
    <title>Pyraminx Start Finder</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0">
    <style>
body {
    line-height: 1.7em;
    color: #34495e;
    font-size: 16px;
    text-align: center;
    font-family: 'Open Sans', sans-serif;
}
table { border: none; }a
    </style>
</head>
<body>
<h1>Pyraminx Start Finder</h1>
<form class="pure-form pure-form-stacked" style="display: inline-block;">
    <input id="scramble" type="text" name="scramble" size="30" maxlength="40" placeholder="Input scramble"
           value="{{scramble}}">
    <input type="submit" value="Find!" class="pure-button pure-button-primary">
</form>

<div class="pure-g" style="max-width: 900px;margin: 0 auto;">
    <div class="pure-u-1 pure-u-md-1-6">
        <h2>Oka</h2>
        <table style="text-align:left;margin:auto;">
            <tbody>
            % for x in oka_solutions:
            <tr>
                <td>{{x}}</td>
            </tr>
            % end
            </tbody>
        </table>
    </div>
    <div class="pure-u-1 pure-u-md-1-6">
        <h2>Keyhole</h2>
        <table style="text-align:left;margin:auto">
            <tbody>
            % for x in kh_solutions:
            <tr>
                <td>{{x}}</td>
            </tr>
            % end
            </tbody>
        </table>
    </div>
    <div class="pure-u-1 pure-u-md-1-6">
        <h2>Bell</h2>
        <table style="text-align:left;margin:auto">
            <tbody>
            % for x in bell_solutions:
            <tr>
                <td>{{x}}</td>
            </tr>
            % end
            </tbody>
        </table>
    </div>
    <div class="pure-u-1 pure-u-md-1-6">
        <h2>1-Flip</h2>
        <table style="text-align:left;margin:auto">
            <tbody>
            % for x in oneflip_solutions:
            <tr>
                <td>{{x}}</td>
            </tr>
            % end
            </tbody>
        </table>
    </div>
    <div class="pure-u-1 pure-u-md-1-6">
        <h2>V-First</h2>
        <table style="text-align:left;margin:auto">
            <tbody>
            % for x in v_solutions:
            <tr>
                <td>{{x}}</td>
            </tr>
            % end
            </tbody>
        </table>
    </div>
    <div class="pure-u-1 pure-u-md-1-6">
        <h2>Intuitive Top</h2>
        <table style="text-align:left;margin:auto">
            <tbody>
            % for x in intuitive_solutions:
            <tr>
                <td>{{x}}</td>
            </tr>
            % end
            </tbody>
        </table>
    </div>
</div>
</body>
</html>
