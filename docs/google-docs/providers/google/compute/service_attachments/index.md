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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.service_attachments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource type. The server generates this identifier. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="connectedEndpoints" /> | `array` | [Output Only] An array of connections for all the consumers connected to this service attachment. |
| <CopyableCode code="connectionPreference" /> | `string` | The connection preference of service attachment. The value can be set to ACCEPT_AUTOMATIC. An ACCEPT_AUTOMATIC service attachment is one that always accepts the connection from consumer forwarding rules. |
| <CopyableCode code="consumerAcceptLists" /> | `array` | Projects that are allowed to connect to this service attachment. |
| <CopyableCode code="consumerRejectLists" /> | `array` | Projects that are not allowed to connect to this service attachment. The project can be specified using its id or number. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="domainNames" /> | `array` | If specified, the domain name will be used during the integration between the PSC connected endpoints and the Cloud DNS. For example, this is a valid domain name: "p.mycompany.com.". Current max number of domain names supported is 1. |
| <CopyableCode code="enableProxyProtocol" /> | `boolean` | If true, enable the proxy protocol which is for supplying client TCP/IP address data in TCP connections that traverse proxies on their way to destination servers. |
| <CopyableCode code="fingerprint" /> | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a ServiceAttachment. An up-to-date fingerprint must be provided in order to patch/update the ServiceAttachment; otherwise, the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve the ServiceAttachment. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#serviceAttachment for service attachments. |
| <CopyableCode code="natSubnets" /> | `array` | An array of URLs where each entry is the URL of a subnet provided by the service producer to use for NAT in this service attachment. |
| <CopyableCode code="producerForwardingRule" /> | `string` | The URL of a forwarding rule with loadBalancingScheme INTERNAL* that is serving the endpoint identified by this service attachment. |
| <CopyableCode code="pscServiceAttachmentId" /> | `object` |  |
| <CopyableCode code="reconcileConnections" /> | `boolean` | This flag determines whether a consumer accept/reject list change can reconcile the statuses of existing ACCEPTED or REJECTED PSC endpoints. - If false, connection policy update will only affect existing PENDING PSC endpoints. Existing ACCEPTED/REJECTED endpoints will remain untouched regardless how the connection policy is modified . - If true, update will affect both PENDING and ACCEPTED/REJECTED PSC endpoints. For example, an ACCEPTED PSC endpoint will be moved to REJECTED if its project is added to the reject list. For newly created service attachment, this boolean defaults to true. |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the service attachment resides. This field applies only to the region resource. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="targetService" /> | `string` | The URL of a service serving the endpoint identified by this service attachment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of all ServiceAttachment resources, regional and global, available to the specified project. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, region, serviceAttachment" /> | Returns the specified ServiceAttachment resource in the given scope. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Lists the ServiceAttachments for a project in the given scope. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a ServiceAttachment in the specified project in the given scope using the parameters that are included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, region, serviceAttachment" /> | Deletes the specified ServiceAttachment in the given scope |
| <CopyableCode code="_aggregated_list" /> | `EXEC` | <CopyableCode code="project" /> | Retrieves the list of all ServiceAttachment resources, regional and global, available to the specified project. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="project, region, serviceAttachment" /> | Patches the specified ServiceAttachment resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |
