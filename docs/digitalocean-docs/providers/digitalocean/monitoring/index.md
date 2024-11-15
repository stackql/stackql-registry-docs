---
title: monitoring
hide_title: false
hide_table_of_contents: false
keywords:
  - monitoring
  - digitalocean
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

monitoring service documentation.

:::info Service Summary

<div class="row">
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>44</b></span><br />
</div>
</div>

:::

## Resources
<div class="row">
<div class="providerDocColumn">
<a href="/providers/digitalocean/monitoring/alerts/">alerts</a><br />
<a href="/providers/digitalocean/monitoring/metrics_apps_cpu_percentages/">metrics_apps_cpu_percentages</a><br />
<a href="/providers/digitalocean/monitoring/metrics_apps_memory_percentages/">metrics_apps_memory_percentages</a><br />
<a href="/providers/digitalocean/monitoring/metrics_apps_restart_counts/">metrics_apps_restart_counts</a><br />
<a href="/providers/digitalocean/monitoring/metrics_droplet_bandwidths/">metrics_droplet_bandwidths</a><br />
<a href="/providers/digitalocean/monitoring/metrics_droplet_cpus/">metrics_droplet_cpus</a><br />
<a href="/providers/digitalocean/monitoring/metrics_droplet_filesystem_free/">metrics_droplet_filesystem_free</a><br />
<a href="/providers/digitalocean/monitoring/metrics_droplet_filesystem_sizes/">metrics_droplet_filesystem_sizes</a><br />
<a href="/providers/digitalocean/monitoring/metrics_droplet_load_15s/">metrics_droplet_load_15s</a><br />
<a href="/providers/digitalocean/monitoring/metrics_droplet_load_1s/">metrics_droplet_load_1s</a><br />
<a href="/providers/digitalocean/monitoring/metrics_droplet_load_5s/">metrics_droplet_load_5s</a><br />
<a href="/providers/digitalocean/monitoring/metrics_droplet_memory_available/">metrics_droplet_memory_available</a><br />
<a href="/providers/digitalocean/monitoring/metrics_droplet_memory_cached/">metrics_droplet_memory_cached</a><br />
<a href="/providers/digitalocean/monitoring/metrics_droplet_memory_free/">metrics_droplet_memory_free</a><br />
<a href="/providers/digitalocean/monitoring/metrics_droplet_memory_totals/">metrics_droplet_memory_totals</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_droplets_connections/">metrics_load_balancer_droplets_connections</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_droplets_downtimes/">metrics_load_balancer_droplets_downtimes</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_droplets_health_checks/">metrics_load_balancer_droplets_health_checks</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_droplets_http_response_time_50ps/">metrics_load_balancer_droplets_http_response_time_50ps</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_droplets_http_response_time_95ps/">metrics_load_balancer_droplets_http_response_time_95ps</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_droplets_http_response_time_99ps/">metrics_load_balancer_droplets_http_response_time_99ps</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_droplets_http_response_time_avgs/">metrics_load_balancer_droplets_http_response_time_avgs</a>
</div>
<div class="providerDocColumn">
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_droplets_http_responses/">metrics_load_balancer_droplets_http_responses</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_droplets_http_session_duration_50ps/">metrics_load_balancer_droplets_http_session_duration_50ps</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_droplets_http_session_duration_95ps/">metrics_load_balancer_droplets_http_session_duration_95ps</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_droplets_http_session_duration_avgs/">metrics_load_balancer_droplets_http_session_duration_avgs</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_droplets_queue_sizes/">metrics_load_balancer_droplets_queue_sizes</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_frontend_connections_current/">metrics_load_balancer_frontend_connections_current</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_frontend_connections_limits/">metrics_load_balancer_frontend_connections_limits</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_frontend_cpu_utilization/">metrics_load_balancer_frontend_cpu_utilization</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_frontend_firewall_dropped_bytes/">metrics_load_balancer_frontend_firewall_dropped_bytes</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_frontend_firewall_dropped_packets/">metrics_load_balancer_frontend_firewall_dropped_packets</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_frontend_http_requests_per_seconds/">metrics_load_balancer_frontend_http_requests_per_seconds</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_frontend_http_responses/">metrics_load_balancer_frontend_http_responses</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_frontend_network_throughput_http/">metrics_load_balancer_frontend_network_throughput_http</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_frontend_network_throughput_tcp/">metrics_load_balancer_frontend_network_throughput_tcp</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_frontend_network_throughput_udp/">metrics_load_balancer_frontend_network_throughput_udp</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_frontend_nlb_tcp_network_throughput/">metrics_load_balancer_frontend_nlb_tcp_network_throughput</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_frontend_nlb_udp_network_throughput/">metrics_load_balancer_frontend_nlb_udp_network_throughput</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_frontend_tls_connections_current/">metrics_load_balancer_frontend_tls_connections_current</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_frontend_tls_connections_exceeding_rate_limits/">metrics_load_balancer_frontend_tls_connections_exceeding_rate_limits</a><br />
<a href="/providers/digitalocean/monitoring/metrics_load_balancer_frontend_tls_connections_limits/">metrics_load_balancer_frontend_tls_connections_limits</a><br />
<a href="/providers/digitalocean/monitoring/sinks/">sinks</a><br />
<a href="/providers/digitalocean/monitoring/sinks_destinations/">sinks_destinations</a>
</div>
</div>