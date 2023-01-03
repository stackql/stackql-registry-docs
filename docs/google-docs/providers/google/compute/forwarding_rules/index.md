---
title: forwarding_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - forwarding_rules
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>forwarding_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.forwarding_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. For Private Service Connect forwarding rules that forward traffic to Google APIs, the forwarding rule name must be a 1-20 characters string with lowercase letters and numbers and must start with a letter. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `IPAddress` | `string` | IP address for which this forwarding rule accepts traffic. When a client sends traffic to this IP address, the forwarding rule directs the traffic to the referenced target or backendService. While creating a forwarding rule, specifying an IPAddress is required under the following circumstances: - When the target is set to targetGrpcProxy and validateForProxyless is set to true, the IPAddress should be set to 0.0.0.0. - When the target is a Private Service Connect Google APIs bundle, you must specify an IPAddress. Otherwise, you can optionally specify an IP address that references an existing static (reserved) IP address resource. When omitted, Google Cloud assigns an ephemeral IP address. Use one of the following formats to specify an IP address while creating a forwarding rule: * IP address number, as in `100.1.2.3` * Full resource URL, as in https://www.googleapis.com/compute/v1/projects/project_id/regions/region /addresses/address-name * Partial URL or by name, as in: - projects/project_id/regions/region/addresses/address-name - regions/region/addresses/address-name - global/addresses/address-name - address-name The forwarding rule's target or backendService, and in most cases, also the loadBalancingScheme, determine the type of IP address that you can use. For detailed information, see [IP address specifications](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications). When reading an IPAddress, the API always returns the IP address number. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#forwardingRule for Forwarding Rule resources. |
| `isMirroringCollector` | `boolean` | Indicates whether or not this load balancer can be used as a collector for packet mirroring. To prevent mirroring loops, instances behind this load balancer will not have their traffic mirrored even if a PacketMirroring rule applies to them. This can only be set to true for load balancers that have their loadBalancingScheme set to INTERNAL. |
| `allowGlobalAccess` | `boolean` | This field is used along with the backend_service field for internal load balancing or with the target field for internal TargetInstance. If the field is set to TRUE, clients can access ILB from all regions. Otherwise only allows access from clients in the same region as the internal load balancer. |
| `allPorts` | `boolean` | This field is used along with the backend_service field for Internal TCP/UDP Load Balancing or Network Load Balancing, or with the target field for internal and external TargetInstance. You can only use one of ports and port_range, or allPorts. The three are mutually exclusive. For TCP, UDP and SCTP traffic, packets addressed to any ports will be forwarded to the target or backendService. |
| `metadataFilters` | `array` | Opaque filter criteria used by load balancer to restrict routing configuration to a limited set of xDS compliant clients. In their xDS requests to load balancer, xDS clients present node metadata. When there is a match, the relevant configuration is made available to those proxies. Otherwise, all the resources (e.g. TargetHttpProxy, UrlMap) referenced by the ForwardingRule are not visible to those proxies. For each metadataFilter in this list, if its filterMatchCriteria is set to MATCH_ANY, at least one of the filterLabels must match the corresponding label provided in the metadata. If its filterMatchCriteria is set to MATCH_ALL, then all of its filterLabels must match with corresponding labels provided in the metadata. If multiple metadataFilters are specified, all of them need to be satisfied in order to be considered a match. metadataFilters specified here will be applifed before those specified in the UrlMap that this ForwardingRule references. metadataFilters only applies to Loadbalancers that have their loadBalancingScheme set to INTERNAL_SELF_MANAGED. |
| `region` | `string` | [Output Only] URL of the region where the regional forwarding rule resides. This field is not applicable to global forwarding rules. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `serviceLabel` | `string` | An optional prefix to the service name for this Forwarding Rule. If specified, the prefix is the first label of the fully qualified service name. The label must be 1-63 characters long, and comply with RFC1035. Specifically, the label must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. This field is only used for internal load balancing. |
| `subnetwork` | `string` | This field identifies the subnetwork that the load balanced IP should belong to for this Forwarding Rule, used in internal load balancing and network load balancing with IPv6. If the network specified is in auto subnet mode, this field is optional. However, a subnetwork must be specified if the network is in custom subnet mode or when creating external forwarding rule with IPv6. |
| `ports` | `array` | The ports field is only supported when the forwarding rule references a backend_service directly. Only packets addressed to the [specified list of ports]((https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications)) are forwarded to backends. You can only use one of ports and port_range, or allPorts. The three are mutually exclusive. You can specify a list of up to five ports, which can be non-contiguous. Forwarding rules with the same [IPAddress, IPProtocol] pair must have disjoint ports. @pattern: \\d+(?:-\\d+)? |
| `network` | `string` | This field is not used for external load balancing. For Internal TCP/UDP Load Balancing, this field identifies the network that the load balanced IP should belong to for this Forwarding Rule. If this field is not specified, the default network will be used. For Private Service Connect forwarding rules that forward traffic to Google APIs, a network must be provided. |
| `networkTier` | `string` | This signifies the networking tier used for configuring this load balancer and can only take the following values: PREMIUM, STANDARD. For regional ForwardingRule, the valid values are PREMIUM and STANDARD. For GlobalForwardingRule, the valid value is PREMIUM. If this field is not specified, it is assumed to be PREMIUM. If IPAddress is specified, this value must be equal to the networkTier of the Address. |
| `ipVersion` | `string` | The IP Version that will be used by this forwarding rule. Valid options are IPV4 or IPV6. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `portRange` | `string` | This field can be used only if: - Load balancing scheme is one of EXTERNAL, INTERNAL_SELF_MANAGED or INTERNAL_MANAGED - IPProtocol is one of TCP, UDP, or SCTP. Packets addressed to ports in the specified range will be forwarded to target or backend_service. You can only use one of ports, port_range, or allPorts. The three are mutually exclusive. Forwarding rules with the same [IPAddress, IPProtocol] pair must have disjoint ports. Some types of forwarding target have constraints on the acceptable ports. For more information, see [Port specifications](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications). @pattern: \\d+(?:-\\d+)? |
| `serviceName` | `string` | [Output Only] The internal fully qualified service name for this Forwarding Rule. This field is only used for internal load balancing. |
| `pscConnectionStatus` | `string` |  |
| `backendService` | `string` | Identifies the backend service to which the forwarding rule sends traffic. Required for Internal TCP/UDP Load Balancing and Network Load Balancing; must be omitted for all other load balancer types. |
| `target` | `string` |  |
| `serviceDirectoryRegistrations` | `array` | Service Directory resources to register this forwarding rule with. Currently, only supports a single Service Directory resource. |
| `labelFingerprint` | `string` | A fingerprint for the labels being applied to this resource, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a ForwardingRule. |
| `pscConnectionId` | `string` | [Output Only] The PSC connection id of the PSC Forwarding Rule. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `fingerprint` | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a ForwardingRule. Include the fingerprint in patch request to ensure that you do not overwrite changes that were applied from another concurrent request. To see the latest fingerprint, make a get() request to retrieve a ForwardingRule. |
| `noAutomateDnsZone` | `boolean` | This is used in PSC consumer ForwardingRule to control whether it should try to auto-generate a DNS zone or not. Non-PSC forwarding rules do not use this field. |
| `labels` | `object` | Labels for this resource. These can only be added or modified by the setLabels method. Each label key/value pair must comply with RFC1035. Label values may be empty. |
| `IPProtocol` | `string` | The IP protocol to which this rule applies. For protocol forwarding, valid options are TCP, UDP, ESP, AH, SCTP, ICMP and L3_DEFAULT. The valid IP protocols are different for different load balancing products as described in [Load balancing features](https://cloud.google.com/load-balancing/docs/features#protocols_from_the_load_balancer_to_the_backends). |
| `loadBalancingScheme` | `string` | Specifies the forwarding rule type. For more information about forwarding rules, refer to Forwarding rule concepts. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `forwardingRules_aggregatedList` | `SELECT` | `project` | Retrieves an aggregated list of forwarding rules. |
| `forwardingRules_get` | `SELECT` | `forwardingRule, project, region` | Returns the specified ForwardingRule resource. |
| `forwardingRules_list` | `SELECT` | `project, region` | Retrieves a list of ForwardingRule resources available to the specified project and region. |
| `forwardingRules_insert` | `INSERT` | `project, region` | Creates a ForwardingRule resource in the specified project and region using the data included in the request. |
| `forwardingRules_delete` | `DELETE` | `forwardingRule, project, region` | Deletes the specified ForwardingRule resource. |
| `forwardingRules_patch` | `EXEC` | `forwardingRule, project, region` | Updates the specified forwarding rule with the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. Currently, you can only patch the network_tier field. |
| `forwardingRules_setLabels` | `EXEC` | `project, region, resource` | Sets the labels on the specified resource. To learn more about labels, read the Labeling Resources documentation. |
| `forwardingRules_setTarget` | `EXEC` | `forwardingRule, project, region` | Changes target URL for forwarding rule. The new target should be of the same type as the old target. |
