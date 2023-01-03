---
title: interconnects
hide_title: false
hide_table_of_contents: false
keywords:
  - interconnects
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
<tr><td><b>Name</b></td><td><code>interconnects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.interconnects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `interconnectType` | `string` | Type of interconnect, which can take one of the following values: - PARTNER: A partner-managed interconnection shared between customers though a partner. - DEDICATED: A dedicated physical interconnection with the customer. Note that a value IT_PRIVATE has been deprecated in favor of DEDICATED. |
| `linkType` | `string` | Type of link requested, which can take one of the following values: - LINK_TYPE_ETHERNET_10G_LR: A 10G Ethernet with LR optics - LINK_TYPE_ETHERNET_100G_LR: A 100G Ethernet with LR optics. Note that this field indicates the speed of each of the links in the bundle, not the speed of the entire bundle. |
| `interconnectAttachments` | `array` | [Output Only] A list of the URLs of all InterconnectAttachments configured to use this Interconnect. |
| `adminEnabled` | `boolean` | Administrative status of the interconnect. When this is set to true, the Interconnect is functional and can carry traffic. When set to false, no packets can be carried over the interconnect and no BGP routes are exchanged over it. By default, the status is set to true. |
| `location` | `string` | URL of the InterconnectLocation object that represents where this connection is to be provisioned. |
| `googleReferenceId` | `string` | [Output Only] Google reference ID to be used when raising support tickets with Google or otherwise to debug backend connectivity issues. |
| `googleIpAddress` | `string` | [Output Only] IP address configured on the Google side of the Interconnect link. This can be used only for ping tests. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `state` | `string` | [Output Only] The current state of Interconnect functionality, which can take one of the following values: - ACTIVE: The Interconnect is valid, turned up and ready to use. Attachments may be provisioned on this Interconnect. - UNPROVISIONED: The Interconnect has not completed turnup. No attachments may be provisioned on this Interconnect. - UNDER_MAINTENANCE: The Interconnect is undergoing internal maintenance. No attachments may be provisioned or updated on this Interconnect.  |
| `customerName` | `string` | Customer name, to put in the Letter of Authorization as the party authorized to request a crossconnect. |
| `nocContactEmail` | `string` | Email address to contact the customer NOC for operations and maintenance notifications regarding this Interconnect. If specified, this will be used for notifications in addition to all other forms described, such as Stackdriver logs alerting and Cloud Notifications. |
| `provisionedLinkCount` | `integer` | [Output Only] Number of links actually provisioned in this interconnect. |
| `operationalStatus` | `string` | [Output Only] The current status of this Interconnect's functionality, which can take one of the following values: - OS_ACTIVE: A valid Interconnect, which is turned up and is ready to use. Attachments may be provisioned on this Interconnect. - OS_UNPROVISIONED: An Interconnect that has not completed turnup. No attachments may be provisioned on this Interconnect. - OS_UNDER_MAINTENANCE: An Interconnect that is undergoing internal maintenance. No attachments may be provisioned or updated on this Interconnect.  |
| `expectedOutages` | `array` | [Output Only] A list of outages expected for this Interconnect. |
| `requestedLinkCount` | `integer` | Target number of physical links in the link bundle, as requested by the customer. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `circuitInfos` | `array` | [Output Only] A list of CircuitInfo objects, that describe the individual circuits in this LAG. |
| `peerIpAddress` | `string` | [Output Only] IP address configured on the customer side of the Interconnect link. The customer should configure this IP address during turnup when prompted by Google NOC. This can be used only for ping tests. |
| `satisfiesPzs` | `boolean` | [Output Only] Set to true if the resource satisfies the zone separation organization policy constraints and false otherwise. Defaults to false if the field is not present. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#interconnect for interconnects. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `interconnect, project` | Returns the specified interconnect. Get a list of available interconnects by making a list() request. |
| `list` | `SELECT` | `project` | Retrieves the list of interconnect available to the specified project. |
| `insert` | `INSERT` | `project` | Creates a Interconnect in the specified project using the data included in the request. |
| `delete` | `DELETE` | `interconnect, project` | Deletes the specified interconnect. |
| `patch` | `EXEC` | `interconnect, project` | Updates the specified interconnect with the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
