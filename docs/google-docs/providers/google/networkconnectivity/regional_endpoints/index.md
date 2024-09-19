---
title: regional_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - regional_endpoints
  - networkconnectivity
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>regional_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>regional_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkconnectivity.regional_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of a RegionalEndpoint. Format: `projects/{project}/locations/{location}/regionalEndpoints/{regional_endpoint}`. |
| <CopyableCode code="description" /> | `string` | Optional. A description of this resource. |
| <CopyableCode code="accessType" /> | `string` | Required. The access type of this regional endpoint. This field is reflected in the PSC Forwarding Rule configuration to enable global access. |
| <CopyableCode code="address" /> | `string` | Optional. The IP Address of the Regional Endpoint. When no address is provided, an IP from the subnetwork is allocated. Use one of the following formats: * IPv4 address as in `10.0.0.1` * Address resource URI as in `projects/{project}/regions/{region}/addresses/{address_name}` |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the RegionalEndpoint was created. |
| <CopyableCode code="ipAddress" /> | `string` | Output only. The literal IP address of the PSC Forwarding Rule created on behalf of the customer. This field is deprecated. Use address instead. |
| <CopyableCode code="labels" /> | `object` | User-defined labels. |
| <CopyableCode code="network" /> | `string` | The name of the VPC network for this private regional endpoint. Format: `projects/{project}/global/networks/{network}` |
| <CopyableCode code="pscForwardingRule" /> | `string` | Output only. The resource reference of the PSC Forwarding Rule created on behalf of the customer. Format: `//compute.googleapis.com/projects/{project}/regions/{region}/forwardingRules/{forwarding_rule_name}` |
| <CopyableCode code="subnetwork" /> | `string` | The name of the subnetwork from which the IP address will be allocated. Format: `projects/{project}/regions/{region}/subnetworks/{subnetwork}` |
| <CopyableCode code="targetGoogleApi" /> | `string` | Required. The service endpoint this private regional endpoint connects to. Format: `{apiname}.{region}.p.rep.googleapis.com` Example: "cloudkms.us-central1.p.rep.googleapis.com". |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the RegionalEndpoint was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, regionalEndpointsId" /> | Gets details of a single RegionalEndpoint. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists RegionalEndpoints in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new RegionalEndpoint in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, regionalEndpointsId" /> | Deletes a single RegionalEndpoint. |

## `SELECT` examples

Lists RegionalEndpoints in a given project and location.

```sql
SELECT
name,
description,
accessType,
address,
createTime,
ipAddress,
labels,
network,
pscForwardingRule,
subnetwork,
targetGoogleApi,
updateTime
FROM google.networkconnectivity.regional_endpoints
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>regional_endpoints</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.networkconnectivity.regional_endpoints (
locationsId,
projectsId,
labels,
description,
targetGoogleApi,
network,
subnetwork,
accessType,
address
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ labels }}',
'{{ description }}',
'{{ targetGoogleApi }}',
'{{ network }}',
'{{ subnetwork }}',
'{{ accessType }}',
'{{ address }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: labels
      value: object
    - name: description
      value: string
    - name: targetGoogleApi
      value: string
    - name: network
      value: string
    - name: subnetwork
      value: string
    - name: accessType
      value: string
    - name: pscForwardingRule
      value: string
    - name: ipAddress
      value: string
    - name: address
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>regional_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM google.networkconnectivity.regional_endpoints
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND regionalEndpointsId = '{{ regionalEndpointsId }}';
```
