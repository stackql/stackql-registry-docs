---
title: subnetworks
hide_title: false
hide_table_of_contents: false
keywords:
  - subnetworks
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
<tr><td><b>Name</b></td><td><code>subnetworks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.subnetworks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | The name of the resource, provided by the client when initially creating the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. This field can be set only at resource creation time. |
| `internalIpv6Prefix` | `string` | [Output Only] The internal IPv6 address range that is assigned to this subnetwork. |
| `privateIpGoogleAccess` | `boolean` | Whether the VMs in this subnet can access Google services without assigned external IP addresses. This field can be both set at resource creation time and updated using setPrivateIpGoogleAccess. |
| `state` | `string` | [Output Only] The state of the subnetwork, which can be one of the following values: READY: Subnetwork is created and ready to use DRAINING: only applicable to subnetworks that have the purpose set to INTERNAL_HTTPS_LOAD_BALANCER and indicates that connections to the load balancer are being drained. A subnetwork that is draining cannot be used or modified until it reaches a status of READY |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `ipCidrRange` | `string` | The range of internal addresses that are owned by this subnetwork. Provide this property when you create the subnetwork. For example, 10.0.0.0/8 or 100.64.0.0/10. Ranges must be unique and non-overlapping within a network. Only IPv4 is supported. This field is set at resource creation time. The range can be any range listed in the Valid ranges list. The range can be expanded after creation using expandIpCidrRange. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#subnetwork for Subnetwork resources. |
| `region` | `string` | URL of the region where the Subnetwork resides. This field can be set only at resource creation time. |
| `ipv6CidrRange` | `string` | [Output Only] This field is for internal use. |
| `privateIpv6GoogleAccess` | `string` | This field is for internal use. This field can be both set at resource creation time and updated using patch. |
| `logConfig` | `object` | The available logging options for this subnetwork. |
| `externalIpv6Prefix` | `string` | [Output Only] The external IPv6 address range that is assigned to this subnetwork. |
| `ipv6AccessType` | `string` | The access type of IPv6 address this subnet holds. It's immutable and can only be specified during creation or the first time the subnet is updated into IPV4_IPV6 dual stack. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `stackType` | `string` | The stack type for the subnet. If set to IPV4_ONLY, new VMs in the subnet are assigned IPv4 addresses only. If set to IPV4_IPV6, new VMs in the subnet can be assigned both IPv4 and IPv6 addresses. If not specified, IPV4_ONLY is used. This field can be both set at resource creation time and updated using patch. |
| `secondaryIpRanges` | `array` | An array of configurations for secondary IP ranges for VM instances contained in this subnetwork. The primary IP of such VM must belong to the primary ipCidrRange of the subnetwork. The alias IPs may belong to either primary or secondary ranges. This field can be updated with a patch request. |
| `network` | `string` | The URL of the network to which this subnetwork belongs, provided by the client when initially creating the subnetwork. This field can be set only at resource creation time. |
| `gatewayAddress` | `string` | [Output Only] The gateway address for default routes to reach destination addresses outside this subnetwork. |
| `purpose` | `string` | The purpose of the resource. This field can be either PRIVATE_RFC_1918 or INTERNAL_HTTPS_LOAD_BALANCER. A subnetwork with purpose set to INTERNAL_HTTPS_LOAD_BALANCER is a user-created subnetwork that is reserved for Internal HTTP(S) Load Balancing. If unspecified, the purpose defaults to PRIVATE_RFC_1918. The enableFlowLogs field isn't supported with the purpose field set to INTERNAL_HTTPS_LOAD_BALANCER. |
| `fingerprint` | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a Subnetwork. An up-to-date fingerprint must be provided in order to update the Subnetwork, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a Subnetwork. |
| `enableFlowLogs` | `boolean` | Whether to enable flow logging for this subnetwork. If this field is not explicitly set, it will not appear in get listings. If not set the default behavior is determined by the org policy, if there is no org policy specified, then it will default to disabled. This field isn't supported with the purpose field set to INTERNAL_HTTPS_LOAD_BALANCER. |
| `role` | `string` | The role of subnetwork. Currently, this field is only used when purpose = INTERNAL_HTTPS_LOAD_BALANCER. The value can be set to ACTIVE or BACKUP. An ACTIVE subnetwork is one that is currently being used for Internal HTTP(S) Load Balancing. A BACKUP subnetwork is one that is ready to be promoted to ACTIVE or is currently draining. This field can be updated with a patch request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `aggregatedList` | `SELECT` | `project` | Retrieves an aggregated list of subnetworks. |
| `get` | `SELECT` | `project, region, subnetwork` | Returns the specified subnetwork. Gets a list of available subnetworks list() request. |
| `list` | `SELECT` | `project, region` | Retrieves a list of subnetworks available to the specified project. |
| `insert` | `INSERT` | `project, region` | Creates a subnetwork in the specified project using the data included in the request. |
| `delete` | `DELETE` | `project, region, subnetwork` | Deletes the specified subnetwork. |
| `expandIpCidrRange` | `EXEC` | `project, region, subnetwork` | Expands the IP CIDR range of the subnetwork to a specified value. |
| `patch` | `EXEC` | `project, region, subnetwork` | Patches the specified subnetwork with the data included in the request. Only certain fields can be updated with a patch request as indicated in the field descriptions. You must specify the current fingerprint of the subnetwork resource being patched. |
| `setPrivateIpGoogleAccess` | `EXEC` | `project, region, subnetwork` | Set whether VMs in this subnet can access Google services without assigning external IP addresses through Private Google Access. |
