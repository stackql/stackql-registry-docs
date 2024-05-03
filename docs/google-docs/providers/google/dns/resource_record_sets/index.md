---
title: resource_record_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_record_sets
  - dns
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
<tr><td><b>Name</b></td><td><code>resource_record_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dns.resource_record_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | For example, www.example.com. |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="routingPolicy" /> | `object` | A RRSetRoutingPolicy represents ResourceRecordSet data that is returned dynamically with the response varying based on configured properties such as geolocation or by weighted random selection. |
| <CopyableCode code="rrdatas" /> | `array` | As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) -- see examples. |
| <CopyableCode code="signatureRrdatas" /> | `array` | As defined in RFC 4034 (section 3.2). |
| <CopyableCode code="ttl" /> | `integer` | Number of seconds that this ResourceRecordSet can be cached by resolvers. |
| <CopyableCode code="type" /> | `string` | The identifier of a supported record type. See the list of Supported DNS record types. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedZone, name, project, type" /> | Fetches the representation of an existing ResourceRecordSet. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="managedZone, project" /> | Enumerates ResourceRecordSets that you have created but not yet deleted. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="managedZone, project" /> | Creates a new ResourceRecordSet. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedZone, name, project, type" /> | Deletes a previously created ResourceRecordSet. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="managedZone, project" /> | Enumerates ResourceRecordSets that you have created but not yet deleted. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="managedZone, name, project, type" /> | Applies a partial update to an existing ResourceRecordSet. |
