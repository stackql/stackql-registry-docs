---
title: resource_value_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_value_configs
  - securitycenter
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

Creates, updates, deletes, gets or lists a <code>resource_value_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_value_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.resource_value_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name for the resource value configuration |
| <CopyableCode code="description" /> | `string` | Description of the resource value configuration. |
| <CopyableCode code="cloudProvider" /> | `string` | Cloud provider this configuration applies to |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp this resource value configuration was created. |
| <CopyableCode code="resourceLabelsSelector" /> | `object` | List of resource labels to search for, evaluated with `AND`. For example, `"resource_labels_selector": {"key": "value", "env": "prod"}` will match resources with labels "key": "value" `AND` "env": "prod" https://cloud.google.com/resource-manager/docs/creating-managing-labels |
| <CopyableCode code="resourceType" /> | `string` | Apply resource_value only to resources that match resource_type. resource_type will be checked with `AND` of other resources. For example, "storage.googleapis.com/Bucket" with resource_value "HIGH" will apply "HIGH" value only to "storage.googleapis.com/Bucket" resources. |
| <CopyableCode code="resourceValue" /> | `string` | Required. Resource value level this expression represents |
| <CopyableCode code="scope" /> | `string` | Project or folder to scope this configuration to. For example, "project/456" would apply this configuration only to resources in "project/456" scope will be checked with `AND` of other resources. |
| <CopyableCode code="sensitiveDataProtectionMapping" /> | `object` | Resource value mapping for Sensitive Data Protection findings. If any of these mappings have a resource value that is not unspecified, the resource_value field will be ignored when reading this configuration. |
| <CopyableCode code="tagValues" /> | `array` | Required. Tag values combined with `AND` to check against. Values in the form "tagValues/123" Example: `[ "tagValues/123", "tagValues/456", "tagValues/789" ]` https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp this resource value configuration was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_resource_value_configs_get" /> | `SELECT` | <CopyableCode code="organizationsId, resourceValueConfigsId" /> | Gets a ResourceValueConfig. |
| <CopyableCode code="organizations_resource_value_configs_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all ResourceValueConfigs. |
| <CopyableCode code="organizations_resource_value_configs_batch_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a ResourceValueConfig for an organization. Maps user's tags to difference resource values for use by the attack path simulation. |
| <CopyableCode code="organizations_resource_value_configs_delete" /> | `DELETE` | <CopyableCode code="organizationsId, resourceValueConfigsId" /> | Deletes a ResourceValueConfig. |
| <CopyableCode code="organizations_resource_value_configs_patch" /> | `UPDATE` | <CopyableCode code="organizationsId, resourceValueConfigsId" /> | Updates an existing ResourceValueConfigs with new rules. |

## `SELECT` examples

Lists all ResourceValueConfigs.

```sql
SELECT
name,
description,
cloudProvider,
createTime,
resourceLabelsSelector,
resourceType,
resourceValue,
scope,
sensitiveDataProtectionMapping,
tagValues,
updateTime
FROM google.securitycenter.resource_value_configs
WHERE organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_value_configs</code> resource.

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
INSERT INTO google.securitycenter.resource_value_configs (
organizationsId,
requests
)
SELECT 
'{{ organizationsId }}',
'{{ requests }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
requests:
  - parent: string
    resourceValueConfig:
      name: string
      resourceValue: string
      tagValues:
        - type: string
      resourceType: string
      scope: string
      resourceLabelsSelector: object
      description: string
      createTime: string
      updateTime: string
      cloudProvider: string
      sensitiveDataProtectionMapping:
        highSensitivityMapping: string
        mediumSensitivityMapping: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>resource_value_configs</code> resource.

```sql
/*+ update */
UPDATE google.securitycenter.resource_value_configs
SET 
name = '{{ name }}',
resourceValue = '{{ resourceValue }}',
tagValues = '{{ tagValues }}',
resourceType = '{{ resourceType }}',
scope = '{{ scope }}',
resourceLabelsSelector = '{{ resourceLabelsSelector }}',
description = '{{ description }}',
cloudProvider = '{{ cloudProvider }}',
sensitiveDataProtectionMapping = '{{ sensitiveDataProtectionMapping }}'
WHERE 
organizationsId = '{{ organizationsId }}'
AND resourceValueConfigsId = '{{ resourceValueConfigsId }}';
```

## `DELETE` example

Deletes the specified <code>resource_value_configs</code> resource.

```sql
/*+ delete */
DELETE FROM google.securitycenter.resource_value_configs
WHERE organizationsId = '{{ organizationsId }}'
AND resourceValueConfigsId = '{{ resourceValueConfigsId }}';
```
