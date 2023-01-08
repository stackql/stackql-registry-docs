---
title: compute
hide_title: false
hide_table_of_contents: false
keywords:
  - compute
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
Creates and runs virtual machines on Google Cloud Platform.   
    
:::info Service Summary

<div class="row">
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>220</b></span><br />
<span>total selectable resources:&nbsp;<b>192</b></span><br />
<span>total methods:&nbsp;<b>729</b></span><br />
</div>
</div>

:::

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>google.compute</code></td></tr>
<tr><td><b>Type</b></td><td>Service</td></tr>
<tr><td><b>Title</b></td><td>Compute Engine API</td></tr>
<tr><td><b>Description</b></td><td>Creates and runs virtual machines on Google Cloud Platform. </td></tr>
<tr><td><b>Id</b></td><td><code>compute:v23.01.00114</code></td></tr>
</tbody></table>

## Resources
<div class="row">
<div class="providerDocColumn">
<a href="/providers/google/compute/accelerator_types/">accelerator_types</a><br />
<a href="/providers/google/compute/addresses/">addresses</a><br />
<a href="/providers/google/compute/autoscalers/">autoscalers</a><br />
<a href="/providers/google/compute/backend_buckets/">backend_buckets</a><br />
<a href="/providers/google/compute/backend_buckets__signed_url_key/">backend_buckets__signed_url_key</a><br />
<a href="/providers/google/compute/backend_services/">backend_services</a><br />
<a href="/providers/google/compute/backend_services__health/">backend_services__health</a><br />
<a href="/providers/google/compute/backend_services__signed_url_key/">backend_services__signed_url_key</a><br />
<a href="/providers/google/compute/backend_services_aggregated/">backend_services_aggregated</a><br />
<a href="/providers/google/compute/backend_services_iam_audit_configs/">backend_services_iam_audit_configs</a><br />
<a href="/providers/google/compute/backend_services_iam_bindings/">backend_services_iam_bindings</a><br />
<a href="/providers/google/compute/backend_services_iam_policies/">backend_services_iam_policies</a><br />
<a href="/providers/google/compute/disk_types/">disk_types</a><br />
<a href="/providers/google/compute/disks/">disks</a><br />
<a href="/providers/google/compute/disks__resource_policies/">disks__resource_policies</a><br />
<a href="/providers/google/compute/disks__snapshot/">disks__snapshot</a><br />
<a href="/providers/google/compute/disks_iam_audit_configs/">disks_iam_audit_configs</a><br />
<a href="/providers/google/compute/disks_iam_bindings/">disks_iam_bindings</a><br />
<a href="/providers/google/compute/disks_iam_policies/">disks_iam_policies</a><br />
<a href="/providers/google/compute/external_vpn_gateways/">external_vpn_gateways</a><br />
<a href="/providers/google/compute/external_vpn_gateways_iam_policies/">external_vpn_gateways_iam_policies</a><br />
<a href="/providers/google/compute/firewall_policies/">firewall_policies</a><br />
<a href="/providers/google/compute/firewall_policies__association/">firewall_policies__association</a><br />
<a href="/providers/google/compute/firewall_policies__associations/">firewall_policies__associations</a><br />
<a href="/providers/google/compute/firewall_policies__rule/">firewall_policies__rule</a><br />
<a href="/providers/google/compute/firewall_policies_iam_audit_configs/">firewall_policies_iam_audit_configs</a><br />
<a href="/providers/google/compute/firewall_policies_iam_bindings/">firewall_policies_iam_bindings</a><br />
<a href="/providers/google/compute/firewall_policies_iam_policies/">firewall_policies_iam_policies</a><br />
<a href="/providers/google/compute/firewalls/">firewalls</a><br />
<a href="/providers/google/compute/forwarding_rules/">forwarding_rules</a><br />
<a href="/providers/google/compute/global_addresses/">global_addresses</a><br />
<a href="/providers/google/compute/global_forwarding_rules/">global_forwarding_rules</a><br />
<a href="/providers/google/compute/global_network_endpoint_groups/">global_network_endpoint_groups</a><br />
<a href="/providers/google/compute/global_network_endpoint_groups__network_endpoints/">global_network_endpoint_groups__network_endpoints</a><br />
<a href="/providers/google/compute/global_operations/">global_operations</a><br />
<a href="/providers/google/compute/global_operations_aggregated/">global_operations_aggregated</a><br />
<a href="/providers/google/compute/global_organization_operations/">global_organization_operations</a><br />
<a href="/providers/google/compute/global_public_delegated_prefixes/">global_public_delegated_prefixes</a><br />
<a href="/providers/google/compute/health_checks/">health_checks</a><br />
<a href="/providers/google/compute/health_checks_aggregated/">health_checks_aggregated</a><br />
<a href="/providers/google/compute/http_health_checks/">http_health_checks</a><br />
<a href="/providers/google/compute/https_health_checks/">https_health_checks</a><br />
<a href="/providers/google/compute/image_family_views/">image_family_views</a><br />
<a href="/providers/google/compute/images/">images</a><br />
<a href="/providers/google/compute/images__from_family/">images__from_family</a><br />
<a href="/providers/google/compute/images_iam_audit_configs/">images_iam_audit_configs</a><br />
<a href="/providers/google/compute/images_iam_bindings/">images_iam_bindings</a><br />
<a href="/providers/google/compute/images_iam_policies/">images_iam_policies</a><br />
<a href="/providers/google/compute/instance_group_managers/">instance_group_managers</a><br />
<a href="/providers/google/compute/instance_group_managers__errors/">instance_group_managers__errors</a><br />
<a href="/providers/google/compute/instance_group_managers__instances/">instance_group_managers__instances</a><br />
<a href="/providers/google/compute/instance_group_managers__managed_instances/">instance_group_managers__managed_instances</a><br />
<a href="/providers/google/compute/instance_group_managers__per_instance_configs/">instance_group_managers__per_instance_configs</a><br />
<a href="/providers/google/compute/instance_groups/">instance_groups</a><br />
<a href="/providers/google/compute/instance_groups__instances/">instance_groups__instances</a><br />
<a href="/providers/google/compute/instance_templates/">instance_templates</a><br />
<a href="/providers/google/compute/instance_templates_iam_audit_configs/">instance_templates_iam_audit_configs</a><br />
<a href="/providers/google/compute/instance_templates_iam_bindings/">instance_templates_iam_bindings</a><br />
<a href="/providers/google/compute/instance_templates_iam_policies/">instance_templates_iam_policies</a><br />
<a href="/providers/google/compute/instances/">instances</a><br />
<a href="/providers/google/compute/instances__access_config/">instances__access_config</a><br />
<a href="/providers/google/compute/instances__effective_firewalls/">instances__effective_firewalls</a><br />
<a href="/providers/google/compute/instances__guest_attributes/">instances__guest_attributes</a><br />
<a href="/providers/google/compute/instances__referrers/">instances__referrers</a><br />
<a href="/providers/google/compute/instances__resource_policies/">instances__resource_policies</a><br />
<a href="/providers/google/compute/instances__screenshot/">instances__screenshot</a><br />
<a href="/providers/google/compute/instances__serial_port_output/">instances__serial_port_output</a><br />
<a href="/providers/google/compute/instances__shielded_instance_identity/">instances__shielded_instance_identity</a><br />
<a href="/providers/google/compute/instances_batch/">instances_batch</a><br />
<a href="/providers/google/compute/instances_iam_audit_configs/">instances_iam_audit_configs</a><br />
<a href="/providers/google/compute/instances_iam_bindings/">instances_iam_bindings</a><br />
<a href="/providers/google/compute/instances_iam_policies/">instances_iam_policies</a><br />
<a href="/providers/google/compute/interconnect_attachments/">interconnect_attachments</a><br />
<a href="/providers/google/compute/interconnect_locations/">interconnect_locations</a><br />
<a href="/providers/google/compute/interconnects/">interconnects</a><br />
<a href="/providers/google/compute/interconnects__diagnostics/">interconnects__diagnostics</a><br />
<a href="/providers/google/compute/license_codes/">license_codes</a><br />
<a href="/providers/google/compute/license_codes_iam_policies/">license_codes_iam_policies</a><br />
<a href="/providers/google/compute/licenses/">licenses</a><br />
<a href="/providers/google/compute/licenses_iam_audit_configs/">licenses_iam_audit_configs</a><br />
<a href="/providers/google/compute/licenses_iam_bindings/">licenses_iam_bindings</a><br />
<a href="/providers/google/compute/licenses_iam_policies/">licenses_iam_policies</a><br />
<a href="/providers/google/compute/machine_images/">machine_images</a><br />
<a href="/providers/google/compute/machine_images_iam_audit_configs/">machine_images_iam_audit_configs</a><br />
<a href="/providers/google/compute/machine_images_iam_bindings/">machine_images_iam_bindings</a><br />
<a href="/providers/google/compute/machine_images_iam_policies/">machine_images_iam_policies</a><br />
<a href="/providers/google/compute/machine_types/">machine_types</a><br />
<a href="/providers/google/compute/network_attachments/">network_attachments</a><br />
<a href="/providers/google/compute/network_attachments_iam_audit_configs/">network_attachments_iam_audit_configs</a><br />
<a href="/providers/google/compute/network_attachments_iam_bindings/">network_attachments_iam_bindings</a><br />
<a href="/providers/google/compute/network_attachments_iam_policies/">network_attachments_iam_policies</a><br />
<a href="/providers/google/compute/network_edge_security_services/">network_edge_security_services</a><br />
<a href="/providers/google/compute/network_endpoint_groups/">network_endpoint_groups</a><br />
<a href="/providers/google/compute/network_endpoint_groups__network_endpoints/">network_endpoint_groups__network_endpoints</a><br />
<a href="/providers/google/compute/network_endpoint_groups_iam_policies/">network_endpoint_groups_iam_policies</a><br />
<a href="/providers/google/compute/network_firewall_policies/">network_firewall_policies</a><br />
<a href="/providers/google/compute/network_firewall_policies__association/">network_firewall_policies__association</a><br />
<a href="/providers/google/compute/network_firewall_policies__rule/">network_firewall_policies__rule</a><br />
<a href="/providers/google/compute/network_firewall_policies_iam_audit_configs/">network_firewall_policies_iam_audit_configs</a><br />
<a href="/providers/google/compute/network_firewall_policies_iam_bindings/">network_firewall_policies_iam_bindings</a><br />
<a href="/providers/google/compute/network_firewall_policies_iam_policies/">network_firewall_policies_iam_policies</a><br />
<a href="/providers/google/compute/networks/">networks</a><br />
<a href="/providers/google/compute/networks__effective_firewalls/">networks__effective_firewalls</a><br />
<a href="/providers/google/compute/networks__peering/">networks__peering</a><br />
<a href="/providers/google/compute/networks__peering_routes/">networks__peering_routes</a><br />
<a href="/providers/google/compute/node_groups/">node_groups</a><br />
<a href="/providers/google/compute/node_groups__nodes/">node_groups__nodes</a><br />
<a href="/providers/google/compute/node_groups_iam_audit_configs/">node_groups_iam_audit_configs</a><br />
<a href="/providers/google/compute/node_groups_iam_bindings/">node_groups_iam_bindings</a><br />
<a href="/providers/google/compute/node_groups_iam_policies/">node_groups_iam_policies</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/google/compute/node_templates/">node_templates</a><br />
<a href="/providers/google/compute/node_templates_iam_audit_configs/">node_templates_iam_audit_configs</a><br />
<a href="/providers/google/compute/node_templates_iam_bindings/">node_templates_iam_bindings</a><br />
<a href="/providers/google/compute/node_templates_iam_policies/">node_templates_iam_policies</a><br />
<a href="/providers/google/compute/node_types/">node_types</a><br />
<a href="/providers/google/compute/packet_mirrorings/">packet_mirrorings</a><br />
<a href="/providers/google/compute/packet_mirrorings_iam_policies/">packet_mirrorings_iam_policies</a><br />
<a href="/providers/google/compute/projects/">projects</a><br />
<a href="/providers/google/compute/projects__xpn_host/">projects__xpn_host</a><br />
<a href="/providers/google/compute/projects__xpn_hosts/">projects__xpn_hosts</a><br />
<a href="/providers/google/compute/projects__xpn_resources/">projects__xpn_resources</a><br />
<a href="/providers/google/compute/public_advertised_prefixes/">public_advertised_prefixes</a><br />
<a href="/providers/google/compute/public_delegated_prefixes/">public_delegated_prefixes</a><br />
<a href="/providers/google/compute/region_autoscalers/">region_autoscalers</a><br />
<a href="/providers/google/compute/region_backend_services/">region_backend_services</a><br />
<a href="/providers/google/compute/region_backend_services__health/">region_backend_services__health</a><br />
<a href="/providers/google/compute/region_backend_services_iam_audit_configs/">region_backend_services_iam_audit_configs</a><br />
<a href="/providers/google/compute/region_backend_services_iam_bindings/">region_backend_services_iam_bindings</a><br />
<a href="/providers/google/compute/region_backend_services_iam_policies/">region_backend_services_iam_policies</a><br />
<a href="/providers/google/compute/region_commitments/">region_commitments</a><br />
<a href="/providers/google/compute/region_disk_types/">region_disk_types</a><br />
<a href="/providers/google/compute/region_disks/">region_disks</a><br />
<a href="/providers/google/compute/region_disks__resource_policies/">region_disks__resource_policies</a><br />
<a href="/providers/google/compute/region_disks__snapshot/">region_disks__snapshot</a><br />
<a href="/providers/google/compute/region_disks_iam_audit_configs/">region_disks_iam_audit_configs</a><br />
<a href="/providers/google/compute/region_disks_iam_bindings/">region_disks_iam_bindings</a><br />
<a href="/providers/google/compute/region_disks_iam_policies/">region_disks_iam_policies</a><br />
<a href="/providers/google/compute/region_health_check_services/">region_health_check_services</a><br />
<a href="/providers/google/compute/region_health_checks/">region_health_checks</a><br />
<a href="/providers/google/compute/region_instance_group_managers/">region_instance_group_managers</a><br />
<a href="/providers/google/compute/region_instance_group_managers__errors/">region_instance_group_managers__errors</a><br />
<a href="/providers/google/compute/region_instance_group_managers__instances/">region_instance_group_managers__instances</a><br />
<a href="/providers/google/compute/region_instance_group_managers__managed_instances/">region_instance_group_managers__managed_instances</a><br />
<a href="/providers/google/compute/region_instance_group_managers__per_instance_configs/">region_instance_group_managers__per_instance_configs</a><br />
<a href="/providers/google/compute/region_instance_groups/">region_instance_groups</a><br />
<a href="/providers/google/compute/region_instance_groups__instances/">region_instance_groups__instances</a><br />
<a href="/providers/google/compute/region_instances/">region_instances</a><br />
<a href="/providers/google/compute/region_network_endpoint_groups/">region_network_endpoint_groups</a><br />
<a href="/providers/google/compute/region_network_firewall_policies/">region_network_firewall_policies</a><br />
<a href="/providers/google/compute/region_network_firewall_policies__association/">region_network_firewall_policies__association</a><br />
<a href="/providers/google/compute/region_network_firewall_policies__effective_firewalls/">region_network_firewall_policies__effective_firewalls</a><br />
<a href="/providers/google/compute/region_network_firewall_policies__rule/">region_network_firewall_policies__rule</a><br />
<a href="/providers/google/compute/region_network_firewall_policies_iam_audit_configs/">region_network_firewall_policies_iam_audit_configs</a><br />
<a href="/providers/google/compute/region_network_firewall_policies_iam_bindings/">region_network_firewall_policies_iam_bindings</a><br />
<a href="/providers/google/compute/region_network_firewall_policies_iam_policies/">region_network_firewall_policies_iam_policies</a><br />
<a href="/providers/google/compute/region_notification_endpoints/">region_notification_endpoints</a><br />
<a href="/providers/google/compute/region_operations/">region_operations</a><br />
<a href="/providers/google/compute/region_security_policies/">region_security_policies</a><br />
<a href="/providers/google/compute/region_ssl_certificates/">region_ssl_certificates</a><br />
<a href="/providers/google/compute/region_ssl_policies/">region_ssl_policies</a><br />
<a href="/providers/google/compute/region_ssl_policies__available_features/">region_ssl_policies__available_features</a><br />
<a href="/providers/google/compute/region_target_http_proxies/">region_target_http_proxies</a><br />
<a href="/providers/google/compute/region_target_https_proxies/">region_target_https_proxies</a><br />
<a href="/providers/google/compute/region_target_tcp_proxies/">region_target_tcp_proxies</a><br />
<a href="/providers/google/compute/region_url_maps/">region_url_maps</a><br />
<a href="/providers/google/compute/regions/">regions</a><br />
<a href="/providers/google/compute/reservations/">reservations</a><br />
<a href="/providers/google/compute/reservations_iam_audit_configs/">reservations_iam_audit_configs</a><br />
<a href="/providers/google/compute/reservations_iam_bindings/">reservations_iam_bindings</a><br />
<a href="/providers/google/compute/reservations_iam_policies/">reservations_iam_policies</a><br />
<a href="/providers/google/compute/resource_policies/">resource_policies</a><br />
<a href="/providers/google/compute/resource_policies_iam_audit_configs/">resource_policies_iam_audit_configs</a><br />
<a href="/providers/google/compute/resource_policies_iam_bindings/">resource_policies_iam_bindings</a><br />
<a href="/providers/google/compute/resource_policies_iam_policies/">resource_policies_iam_policies</a><br />
<a href="/providers/google/compute/routers/">routers</a><br />
<a href="/providers/google/compute/routers__nat_mapping_info/">routers__nat_mapping_info</a><br />
<a href="/providers/google/compute/routers__router_status/">routers__router_status</a><br />
<a href="/providers/google/compute/routes/">routes</a><br />
<a href="/providers/google/compute/security_policies/">security_policies</a><br />
<a href="/providers/google/compute/security_policies__preconfigured_expression_sets/">security_policies__preconfigured_expression_sets</a><br />
<a href="/providers/google/compute/security_policies__rule/">security_policies__rule</a><br />
<a href="/providers/google/compute/security_policies_aggregated/">security_policies_aggregated</a><br />
<a href="/providers/google/compute/service_attachments/">service_attachments</a><br />
<a href="/providers/google/compute/service_attachments_iam_audit_configs/">service_attachments_iam_audit_configs</a><br />
<a href="/providers/google/compute/service_attachments_iam_bindings/">service_attachments_iam_bindings</a><br />
<a href="/providers/google/compute/service_attachments_iam_policies/">service_attachments_iam_policies</a><br />
<a href="/providers/google/compute/snapshots/">snapshots</a><br />
<a href="/providers/google/compute/snapshots_iam_audit_configs/">snapshots_iam_audit_configs</a><br />
<a href="/providers/google/compute/snapshots_iam_bindings/">snapshots_iam_bindings</a><br />
<a href="/providers/google/compute/snapshots_iam_policies/">snapshots_iam_policies</a><br />
<a href="/providers/google/compute/ssl_certificates/">ssl_certificates</a><br />
<a href="/providers/google/compute/ssl_certificates_aggregated/">ssl_certificates_aggregated</a><br />
<a href="/providers/google/compute/ssl_policies/">ssl_policies</a><br />
<a href="/providers/google/compute/ssl_policies__available_features/">ssl_policies__available_features</a><br />
<a href="/providers/google/compute/subnetworks/">subnetworks</a><br />
<a href="/providers/google/compute/subnetworks__usable/">subnetworks__usable</a><br />
<a href="/providers/google/compute/subnetworks_iam_audit_configs/">subnetworks_iam_audit_configs</a><br />
<a href="/providers/google/compute/subnetworks_iam_bindings/">subnetworks_iam_bindings</a><br />
<a href="/providers/google/compute/subnetworks_iam_policies/">subnetworks_iam_policies</a><br />
<a href="/providers/google/compute/target_grpc_proxies/">target_grpc_proxies</a><br />
<a href="/providers/google/compute/target_http_proxies/">target_http_proxies</a><br />
<a href="/providers/google/compute/target_http_proxies_aggregated/">target_http_proxies_aggregated</a><br />
<a href="/providers/google/compute/target_https_proxies/">target_https_proxies</a><br />
<a href="/providers/google/compute/target_https_proxies_aggregated/">target_https_proxies_aggregated</a><br />
<a href="/providers/google/compute/target_instances/">target_instances</a><br />
<a href="/providers/google/compute/target_pools/">target_pools</a><br />
<a href="/providers/google/compute/target_pools__health/">target_pools__health</a><br />
<a href="/providers/google/compute/target_pools__health_check/">target_pools__health_check</a><br />
<a href="/providers/google/compute/target_pools__instance/">target_pools__instance</a><br />
<a href="/providers/google/compute/target_ssl_proxies/">target_ssl_proxies</a><br />
<a href="/providers/google/compute/target_tcp_proxies/">target_tcp_proxies</a><br />
<a href="/providers/google/compute/target_vpn_gateways/">target_vpn_gateways</a><br />
<a href="/providers/google/compute/url_maps/">url_maps</a><br />
<a href="/providers/google/compute/url_maps_aggregated/">url_maps_aggregated</a><br />
<a href="/providers/google/compute/vpn_gateways/">vpn_gateways</a><br />
<a href="/providers/google/compute/vpn_gateways__status/">vpn_gateways__status</a><br />
<a href="/providers/google/compute/vpn_gateways_iam_policies/">vpn_gateways_iam_policies</a><br />
<a href="/providers/google/compute/vpn_tunnels/">vpn_tunnels</a><br />
<a href="/providers/google/compute/zone_operations/">zone_operations</a><br />
<a href="/providers/google/compute/zones/">zones</a><br />
</div>
</div>
