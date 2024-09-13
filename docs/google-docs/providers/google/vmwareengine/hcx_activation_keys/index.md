---
title: hcx_activation_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - hcx_activation_keys
  - vmwareengine
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

Creates, updates, deletes or gets an <code>hcx_activation_key</code> resource or lists <code>hcx_activation_keys</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hcx_activation_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmwareengine.hcx_activation_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of this HcxActivationKey. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1/privateClouds/my-cloud/hcxActivationKeys/my-key` |
| <CopyableCode code="activationKey" /> | `string` | Output only. HCX activation key. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time of HCX activation key. |
| <CopyableCode code="state" /> | `string` | Output only. State of HCX activation key. |
| <CopyableCode code="uid" /> | `string` | Output only. System-generated unique identifier for the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hcxActivationKeysId, locationsId, privateCloudsId, projectsId" /> | Retrieves a `HcxActivationKey` resource by its resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Lists `HcxActivationKey` resources in a given private cloud. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Creates a new HCX activation key in a given private cloud. |

## `SELECT` examples

Lists `HcxActivationKey` resources in a given private cloud.

```sql
SELECT
name,
activationKey,
createTime,
state,
uid
FROM google.vmwareengine.hcx_activation_keys
WHERE locationsId = '{{ locationsId }}'
AND privateCloudsId = '{{ privateCloudsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hcx_activation_keys</code> resource.

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
INSERT INTO google.vmwareengine.hcx_activation_keys (
locationsId,
privateCloudsId,
projectsId,
name,
createTime,
state,
activationKey,
uid
)
SELECT 
'{{ locationsId }}',
'{{ privateCloudsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ state }}',
'{{ activationKey }}',
'{{ uid }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: state
        value: '{{ state }}'
      - name: activationKey
        value: '{{ activationKey }}'
      - name: uid
        value: '{{ uid }}'

```
</TabItem>
</Tabs>
