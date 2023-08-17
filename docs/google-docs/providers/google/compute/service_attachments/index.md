---
title: service_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - service_attachments
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.service_attachments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource type. The server generates this identifier. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `reconcileConnections` | `boolean` | This flag determines whether a consumer accept/reject list change can reconcile the statuses of existing ACCEPTED or REJECTED PSC endpoints. - If false, connection policy update will only affect existing PENDING PSC endpoints. Existing ACCEPTED/REJECTED endpoints will remain untouched regardless how the connection policy is modified . - If true, update will affect both PENDING and ACCEPTED/REJECTED PSC endpoints. For example, an ACCEPTED PSC endpoint will be moved to REJECTED if its project is added to the reject list. For newly created service attachment, this boolean defaults to true. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `connectedEndpoints` | `array` | [Output Only] An array of connections for all the consumers connected to this service attachment. |
| `natSubnets` | `array` | An array of URLs where each entry is the URL of a subnet provided by the service producer to use for NAT in this service attachment. |
| `domainNames` | `array` | If specified, the domain name will be used during the integration between the PSC connected endpoints and the Cloud DNS. For example, this is a valid domain name: "p.mycompany.com.". Current max number of domain names supported is 1. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `targetService` | `string` | The URL of a service serving the endpoint identified by this service attachment. |
| `consumerAcceptLists` | `array` | Projects that are allowed to connect to this service attachment. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#serviceAttachment for service attachments. |
| `consumerRejectLists` | `array` | Projects that are not allowed to connect to this service attachment. The project can be specified using its id or number. |
| `producerForwardingRule` | `string` | The URL of a forwarding rule with loadBalancingScheme INTERNAL* that is serving the endpoint identified by this service attachment. |
| `connectionPreference` | `string` | The connection preference of service attachment. The value can be set to ACCEPT_AUTOMATIC. An ACCEPT_AUTOMATIC service attachment is one that always accepts the connection from consumer forwarding rules. |
| `pscServiceAttachmentId` | `object` |  |
| `fingerprint` | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a ServiceAttachment. An up-to-date fingerprint must be provided in order to patch/update the ServiceAttachment; otherwise, the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve the ServiceAttachment. |
| `enableProxyProtocol` | `boolean` | If true, enable the proxy protocol which is for supplying client TCP/IP address data in TCP connections that traverse proxies on their way to destination servers. |
| `region` | `string` | [Output Only] URL of the region where the service attachment resides. This field applies only to the region resource. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `project, region, serviceAttachment` | Returns the specified ServiceAttachment resource in the given scope. |
| `list` | `SELECT` | `project, region` | Lists the ServiceAttachments for a project in the given scope. |
| `insert` | `INSERT` | `project, region` | Creates a ServiceAttachment in the specified project in the given scope using the parameters that are included in the request. |
| `delete` | `DELETE` | `project, region, serviceAttachment` | Deletes the specified ServiceAttachment in the given scope |
| `_list` | `EXEC` | `project, region` | Lists the ServiceAttachments for a project in the given scope. |
| `aggregated_list` | `EXEC` | `project` | Retrieves the list of all ServiceAttachment resources, regional and global, available to the specified project. |
| `patch` | `EXEC` | `project, region, serviceAttachment` | Patches the specified ServiceAttachment resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |
