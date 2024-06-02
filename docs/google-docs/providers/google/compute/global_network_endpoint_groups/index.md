---
title: global_network_endpoint_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - global_network_endpoint_groups
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_network_endpoint_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="compute.global_network_endpoint_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="annotations" /> | `object` | Metadata defined as annotations on the network endpoint group. |
| <CopyableCode code="appEngine" /> | `object` | Configuration for an App Engine network endpoint group (NEG). The service is optional, may be provided explicitly or in the URL mask. The version is optional and can only be provided explicitly or in the URL mask when service is present. Note: App Engine service must be in the same project and located in the same region as the Serverless NEG. |
| <CopyableCode code="cloudFunction" /> | `object` | Configuration for a Cloud Function network endpoint group (NEG). The function must be provided explicitly or in the URL mask. Note: Cloud Function must be in the same project and located in the same region as the Serverless NEG. |
| <CopyableCode code="cloudRun" /> | `object` | Configuration for a Cloud Run network endpoint group (NEG). The service must be provided explicitly or in the URL mask. The tag is optional, may be provided explicitly or in the URL mask. Note: Cloud Run service must be in the same project and located in the same region as the Serverless NEG. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="defaultPort" /> | `integer` | The default port used if the port number is not specified in the network endpoint. If the network endpoint type is either GCE_VM_IP, SERVERLESS or PRIVATE_SERVICE_CONNECT, this field must not be specified. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#networkEndpointGroup for network endpoint group. |
| <CopyableCode code="network" /> | `string` | The URL of the network to which all network endpoints in the NEG belong. Uses default project network if unspecified. |
| <CopyableCode code="networkEndpointType" /> | `string` | Type of network endpoints in this network endpoint group. Can be one of GCE_VM_IP, GCE_VM_IP_PORT, NON_GCP_PRIVATE_IP_PORT, INTERNET_FQDN_PORT, INTERNET_IP_PORT, SERVERLESS, PRIVATE_SERVICE_CONNECT, GCE_VM_IP_PORTMAP. |
| <CopyableCode code="pscData" /> | `object` | All data that is specifically relevant to only network endpoint groups of type PRIVATE_SERVICE_CONNECT. |
| <CopyableCode code="pscTargetService" /> | `string` | The target service url used to set up private service connection to a Google API or a PSC Producer Service Attachment. An example value is: asia-northeast3-cloudkms.googleapis.com |
| <CopyableCode code="region" /> | `string` | [Output Only] The URL of the region where the network endpoint group is located. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="size" /> | `integer` | [Output only] Number of network endpoints in the network endpoint group. |
| <CopyableCode code="subnetwork" /> | `string` | Optional URL of the subnetwork to which all network endpoints in the NEG belong. |
| <CopyableCode code="zone" /> | `string` | [Output Only] The URL of the zone where the network endpoint group is located. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkEndpointGroup, project" /> | Returns the specified network endpoint group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of network endpoint groups that are located in the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a network endpoint group in the specified project using the parameters that are included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkEndpointGroup, project" /> | Deletes the specified network endpoint group.Note that the NEG cannot be deleted if there are backend services referencing it. |
| <CopyableCode code="attach_network_endpoints" /> | `EXEC` | <CopyableCode code="networkEndpointGroup, project" /> | Attach a network endpoint to the specified network endpoint group. |
| <CopyableCode code="detach_network_endpoints" /> | `EXEC` | <CopyableCode code="networkEndpointGroup, project" /> | Detach the network endpoint from the specified network endpoint group. |
