---
title: subnetworks_usable
hide_title: false
hide_table_of_contents: false
keywords:
  - subnetworks_usable
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
<tr><td><b>Name</b></td><td><code>subnetworks_usable</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.subnetworks_usable</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `purpose` | `string` | The purpose of the resource. This field can be either PRIVATE_RFC_1918 or INTERNAL_HTTPS_LOAD_BALANCER. A subnetwork with purpose set to INTERNAL_HTTPS_LOAD_BALANCER is a user-created subnetwork that is reserved for Internal HTTP(S) Load Balancing. If unspecified, the purpose defaults to PRIVATE_RFC_1918. The enableFlowLogs field isn't supported with the purpose field set to INTERNAL_HTTPS_LOAD_BALANCER. |
| `subnetwork` | `string` | Subnetwork URL. |
| `secondaryIpRanges` | `array` | Secondary IP ranges. |
| `stackType` | `string` | The stack type for the subnet. If set to IPV4_ONLY, new VMs in the subnet are assigned IPv4 addresses only. If set to IPV4_IPV6, new VMs in the subnet can be assigned both IPv4 and IPv6 addresses. If not specified, IPV4_ONLY is used. This field can be both set at resource creation time and updated using patch. |
| `ipv6AccessType` | `string` | The access type of IPv6 address this subnet holds. It's immutable and can only be specified during creation or the first time the subnet is updated into IPV4_IPV6 dual stack. |
| `ipCidrRange` | `string` | The range of internal addresses that are owned by this subnetwork. |
| `role` | `string` | The role of subnetwork. Currently, this field is only used when purpose = INTERNAL_HTTPS_LOAD_BALANCER. The value can be set to ACTIVE or BACKUP. An ACTIVE subnetwork is one that is currently being used for Internal HTTP(S) Load Balancing. A BACKUP subnetwork is one that is ready to be promoted to ACTIVE or is currently draining. This field can be updated with a patch request. |
| `network` | `string` | Network URL. |
| `externalIpv6Prefix` | `string` | [Output Only] The external IPv6 address range that is assigned to this subnetwork. |
| `internalIpv6Prefix` | `string` | [Output Only] The internal IPv6 address range that is assigned to this subnetwork. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `subnetworks_listUsable` | `SELECT` | `project` |
