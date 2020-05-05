<!DOCTYPE html>
<html lang="en">
<head>
        <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="X-UA-Compatible" content="ie-edge">
    <style>
        body {
          font-family: 'Open Sans', sans-serif;
        }

        .graph-title {
          font-weight: bold;
          text-transform: uppercase;
          font-size: 16px;
          fill: black;

        }
        .graph .labels.x-labels {
          text-anchor: middle;
          font-size: 10px;
        }

        .graph .labels.y-labels {
          text-anchor: end;
        }

        .graph {
          height: 500px;
          width: 1500px;
        }

        .graph .grid {
          stroke: black;
          stroke-dasharray: 0;
          stroke-width: 1;
        }

        .sub-xgrid {
          stroke: #ccc;
          stroke-dasharray: 0;
          stroke-width: 0.7;
        }

        .sub-wygrid {
          stroke: #ccc;
          stroke-dasharray: 5.5;
          stroke-width: 0.9;
        }

        .sub-cygrid {
          stroke: #ccc;
          stroke-dasharray: 0;
          stroke-width: 0.7;
        }

        .labels {
          font-size: 13px;
        }

        .label-title {
          font-weight: bold;
          text-transform: uppercase;
          font-size: 12px;
          fill: black;
        }
        .date_label {
          writing-mode: vertical-lr;
          color: #0074d9;
          font-size: 10px;
          display: inline-block
        }
    </style>
</head>
<body>
    <svg viewBox="500 0 500 500" class="graph" aria-labelledby="title" role="img">
      <title id="title">Coronavirus cases </title>
      <text class="graph-title" x="400" y="15">coronavirus cases</text>
    <g class="grid y-grid" id="yGrid">
      <line x1="190" x2="190" y1="25" y2="421"></line>
      <line x1="806" x2="806" y1="25" y2="421"></line>
    </g>
    <g class="grid x-grid" id="xGrid">
      <line x1="190" x2="805" y1="420" y2="420"></line>
    </g>
      <g class="labels x-labels">
          {% for c in range(0, dt_lbl_len) %}
              <text class="date_label" x={{ dic.dt_lbl_loc[c] }} y="452">{{ dic.dt_lbl_pt[0][c]}}</text>
              <line class="sub-xgrid" x1="{{ dic.dt_lbl_loc[c] }}" x2="{{ dic.dt_lbl_loc[c] }}" y1="421" y2="25"></line>
          {% endfor %}
      <text x="155" y="450" class="label-title">Date</text>
    </g>
    <g class="labels y-labels">
      {% for a in  range(0, wld_lbl_len) %}
        <text x="180" y="{{dic.wld_ylbl_loc[a] + 4 }}">{{dic.wld_lbl[a]}}</text>
        <line class="grid x-grid" id="xGrid" x1="190" x2="183" y1="{{dic.wld_ylbl_loc[a]}}" y2="{{dic.wld_ylbl_loc[a]}}" />
        <line class="sub-wygrid" x1="190" x2="805" y1="{{dic.wld_ylbl_loc[a]}}" y2="{{dic.wld_ylbl_loc[a]}}"></line>
      {% endfor %}
      {% for a in  range(0, ctry_lbl_len) %}
        <text x="844" y="{{dic.ctry_ylbl_loc[a] + 4}}">{{dic.ctry_lbl[a]}}</text>
        <line class="grid x-grid" id="xGrid" x1="806" x2="814" y1="{{dic.ctry_ylbl_loc[a]}}" y2="{{dic.ctry_ylbl_loc[a]}}" />
        <line class="sub-cygrid" x1="190" x2="805" y1="{{dic.ctry_ylbl_loc[a]}}" y2="{{dic.ctry_ylbl_loc[a]}}"></line>
      {% endfor %}
      <text  x="250" y="20" class="label-title">World [milhões]</text>
      <text x="870" y="20" class="label-title">by Country [mil]</text>
    </g>
    <g class="data" data-setname="Our first data set">
        {% for c in range(0,ctry_count) %}
            {% for d in range(0, ctry_len[c]-1) %}
                <circle cx="{{ dic.dt_pt[c][d] }}" cy="{{ dic.ctry_pt[c][d] }}" r="0.5" stroke="{{ dic.color[c] }}" fill="{{ dic.color[c] }}"/>
                <line stroke="{{ dic.color[c] }}" stroke-width="2" x1="{{ dic.dt_pt[c][d] }}" y1="{{ dic.ctry_pt[c][d] }}" x2="{{ dic.dt_pt[c][d+1] }}" y2="{{ dic.ctry_pt[c][d+1] }}" />
            {% endfor %}
            <rect stroke="#ccc" stroke-width="1" fill="None" x="900" y="55" height="{{ 24*ctry_count }}" width="100"/>
            <line stroke="{{ dic.color[c] }}" stroke-width="2" x1="910" y1="{{75 + 20 * c}}" x2="935" y2="{{75 + 20 * c}}" />
            <text text-anchor="start" font-weight="bold" fill="{{ dic.color[c] }}" font-size="14" x="943" y="{{80 + 20 * c}}">{{ dic.ctry_list[c] }}</text>
        {% endfor %}
    </g>
    </svg>

<!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>

</html>
