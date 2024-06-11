---
title: ec2
hide_title: false
hide_table_of_contents: false
keywords:
  - ec2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

The ec2 service documentation.

:::info Service Summary

<div class="row">
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>82</b></span><br />
<span>total selectable resources:&nbsp;<b>82</b></span><br />
<span>total methods:&nbsp;<b>82</b></span><br />
</div>
</div>

:::

## Resources
<div class="row">
<div class="providerDocColumn">
<a href="/providers/aws/ec2/capacity_reservation_fleets/">capacity_reservation_fleets</a><br />
<a href="/providers/aws/ec2/capacity_reservations/">capacity_reservations</a><br />
<a href="/providers/aws/ec2/carrier_gateways/">carrier_gateways</a><br />
<a href="/providers/aws/ec2/customer_gateways/">customer_gateways</a><br />
<a href="/providers/aws/ec2/dhcp_options/">dhcp_options</a><br />
<a href="/providers/aws/ec2/ec2fleets/">ec2fleets</a><br />
<a href="/providers/aws/ec2/egress_only_internet_gateways/">egress_only_internet_gateways</a><br />
<a href="/providers/aws/ec2/eip_associations/">eip_associations</a><br />
<a href="/providers/aws/ec2/eips/">eips</a><br />
<a href="/providers/aws/ec2/enclave_certificate_iam_role_associations/">enclave_certificate_iam_role_associations</a><br />
<a href="/providers/aws/ec2/flow_logs/">flow_logs</a><br />
<a href="/providers/aws/ec2/gateway_route_table_associations/">gateway_route_table_associations</a><br />
<a href="/providers/aws/ec2/hosts/">hosts</a><br />
<a href="/providers/aws/ec2/instance_connect_endpoints/">instance_connect_endpoints</a><br />
<a href="/providers/aws/ec2/instances/">instances</a><br />
<a href="/providers/aws/ec2/internet_gateways/">internet_gateways</a><br />
<a href="/providers/aws/ec2/ipam_allocations/">ipam_allocations</a><br />
<a href="/providers/aws/ec2/ipam_pool_cidrs/">ipam_pool_cidrs</a><br />
<a href="/providers/aws/ec2/ipam_pools/">ipam_pools</a><br />
<a href="/providers/aws/ec2/ipam_resource_discoveries/">ipam_resource_discoveries</a><br />
<a href="/providers/aws/ec2/ipam_resource_discovery_associations/">ipam_resource_discovery_associations</a><br />
<a href="/providers/aws/ec2/ipam_scopes/">ipam_scopes</a><br />
<a href="/providers/aws/ec2/ipams/">ipams</a><br />
<a href="/providers/aws/ec2/key_pairs/">key_pairs</a><br />
<a href="/providers/aws/ec2/launch_templates/">launch_templates</a><br />
<a href="/providers/aws/ec2/local_gateway_route_table_virtual_interface_group_associations/">local_gateway_route_table_virtual_interface_group_associations</a><br />
<a href="/providers/aws/ec2/local_gateway_route_tables/">local_gateway_route_tables</a><br />
<a href="/providers/aws/ec2/local_gateway_route_tablevpc_associations/">local_gateway_route_tablevpc_associations</a><br />
<a href="/providers/aws/ec2/local_gateway_routes/">local_gateway_routes</a><br />
<a href="/providers/aws/ec2/nat_gateways/">nat_gateways</a><br />
<a href="/providers/aws/ec2/network_acls/">network_acls</a><br />
<a href="/providers/aws/ec2/network_insights_access_scope_analyses/">network_insights_access_scope_analyses</a><br />
<a href="/providers/aws/ec2/network_insights_access_scopes/">network_insights_access_scopes</a><br />
<a href="/providers/aws/ec2/network_insights_analyses/">network_insights_analyses</a><br />
<a href="/providers/aws/ec2/network_insights_paths/">network_insights_paths</a><br />
<a href="/providers/aws/ec2/network_interface_attachments/">network_interface_attachments</a><br />
<a href="/providers/aws/ec2/network_interfaces/">network_interfaces</a><br />
<a href="/providers/aws/ec2/network_performance_metric_subscriptions/">network_performance_metric_subscriptions</a><br />
<a href="/providers/aws/ec2/placement_groups/">placement_groups</a><br />
<a href="/providers/aws/ec2/prefix_lists/">prefix_lists</a><br />
<a href="/providers/aws/ec2/route_tables/">route_tables</a>
</div>
<div class="providerDocColumn">
<a href="/providers/aws/ec2/routes/">routes</a><br />
<a href="/providers/aws/ec2/security_group_egresses/">security_group_egresses</a><br />
<a href="/providers/aws/ec2/security_group_ingresses/">security_group_ingresses</a><br />
<a href="/providers/aws/ec2/security_groups/">security_groups</a><br />
<a href="/providers/aws/ec2/snapshot_block_public_accesses/">snapshot_block_public_accesses</a><br />
<a href="/providers/aws/ec2/spot_fleets/">spot_fleets</a><br />
<a href="/providers/aws/ec2/subnet_cidr_blocks/">subnet_cidr_blocks</a><br />
<a href="/providers/aws/ec2/subnet_network_acl_associations/">subnet_network_acl_associations</a><br />
<a href="/providers/aws/ec2/subnet_route_table_associations/">subnet_route_table_associations</a><br />
<a href="/providers/aws/ec2/subnets/">subnets</a><br />
<a href="/providers/aws/ec2/transit_gateway_attachments/">transit_gateway_attachments</a><br />
<a href="/providers/aws/ec2/transit_gateway_connects/">transit_gateway_connects</a><br />
<a href="/providers/aws/ec2/transit_gateway_multicast_domain_associations/">transit_gateway_multicast_domain_associations</a><br />
<a href="/providers/aws/ec2/transit_gateway_multicast_domains/">transit_gateway_multicast_domains</a><br />
<a href="/providers/aws/ec2/transit_gateway_multicast_group_members/">transit_gateway_multicast_group_members</a><br />
<a href="/providers/aws/ec2/transit_gateway_multicast_group_sources/">transit_gateway_multicast_group_sources</a><br />
<a href="/providers/aws/ec2/transit_gateway_peering_attachments/">transit_gateway_peering_attachments</a><br />
<a href="/providers/aws/ec2/transit_gateway_route_table_associations/">transit_gateway_route_table_associations</a><br />
<a href="/providers/aws/ec2/transit_gateway_route_table_propagations/">transit_gateway_route_table_propagations</a><br />
<a href="/providers/aws/ec2/transit_gateway_route_tables/">transit_gateway_route_tables</a><br />
<a href="/providers/aws/ec2/transit_gateway_routes/">transit_gateway_routes</a><br />
<a href="/providers/aws/ec2/transit_gateway_vpc_attachments/">transit_gateway_vpc_attachments</a><br />
<a href="/providers/aws/ec2/transit_gateways/">transit_gateways</a><br />
<a href="/providers/aws/ec2/verified_access_endpoints/">verified_access_endpoints</a><br />
<a href="/providers/aws/ec2/verified_access_groups/">verified_access_groups</a><br />
<a href="/providers/aws/ec2/verified_access_instances/">verified_access_instances</a><br />
<a href="/providers/aws/ec2/verified_access_trust_providers/">verified_access_trust_providers</a><br />
<a href="/providers/aws/ec2/volume_attachments/">volume_attachments</a><br />
<a href="/providers/aws/ec2/volumes/">volumes</a><br />
<a href="/providers/aws/ec2/vpc_cidr_blocks/">vpc_cidr_blocks</a><br />
<a href="/providers/aws/ec2/vpc_endpoint_connection_notifications/">vpc_endpoint_connection_notifications</a><br />
<a href="/providers/aws/ec2/vpc_endpoint_service_permissions/">vpc_endpoint_service_permissions</a><br />
<a href="/providers/aws/ec2/vpc_endpoint_services/">vpc_endpoint_services</a><br />
<a href="/providers/aws/ec2/vpc_endpoints/">vpc_endpoints</a><br />
<a href="/providers/aws/ec2/vpc_gateway_attachments/">vpc_gateway_attachments</a><br />
<a href="/providers/aws/ec2/vpc_peering_connections/">vpc_peering_connections</a><br />
<a href="/providers/aws/ec2/vpcdhcp_options_associations/">vpcdhcp_options_associations</a><br />
<a href="/providers/aws/ec2/vpcs/">vpcs</a><br />
<a href="/providers/aws/ec2/vpn_connection_routes/">vpn_connection_routes</a><br />
<a href="/providers/aws/ec2/vpn_connections/">vpn_connections</a><br />
<a href="/providers/aws/ec2/vpn_gateways/">vpn_gateways</a>
</div>
</div>