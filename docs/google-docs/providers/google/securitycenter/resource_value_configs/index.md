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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_value_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.resource_value_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name for the resource value config |
| <CopyableCode code="description" /> | `string` | Description of the resource value config. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp this resource value config was created. |
| <CopyableCode code="resourceLabelsSelector" /> | `object` | List of resource labels to search for, evaluated with AND. E.g. "resource_labels_selector": &#123;"key": "value", "env": "prod"&#125; will match resources with labels "key": "value" AND "env": "prod" https://cloud.google.com/resource-manager/docs/creating-managing-labels |
| <CopyableCode code="resourceType" /> | `string` | Apply resource_value only to resources that match resource_type. resource_type will be checked with "AND" of other resources. E.g. "storage.googleapis.com/Bucket" with resource_value "HIGH" will apply "HIGH" value only to "storage.googleapis.com/Bucket" resources. |
| <CopyableCode code="resourceValue" /> | `string` | Required. Resource value level this expression represents |
| <CopyableCode code="scope" /> | `string` | Project or folder to scope this config to. For example, "project/456" would apply this config only to resources in "project/456" scope will be checked with "AND" of other resources. |
| <CopyableCode code="tagValues" /> | `array` | Required. Tag values combined with AND to check against. Values in the form "tagValues/123" E.g. [ "tagValues/123", "tagValues/456", "tagValues/789" ] https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp this resource value config was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_resource_value_configs_get" /> | `SELECT` | <CopyableCode code="organizationsId, resourceValueConfigsId" /> | Gets a ResourceValueConfig. |
| <CopyableCode code="organizations_resource_value_configs_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all ResourceValueConfigs. |
| <CopyableCode code="organizations_resource_value_configs_delete" /> | `DELETE` | <CopyableCode code="organizationsId, resourceValueConfigsId" /> | Deletes a ResourceValueConfig. |
| <CopyableCode code="_organizations_resource_value_configs_list" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Lists all ResourceValueConfigs. |
| <CopyableCode code="organizations_resource_value_configs_batch_create" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Creates a ResourceValueConfig for an organization. Maps user's tags to difference resource values for use by the attack path simulation. |
| <CopyableCode code="organizations_resource_value_configs_patch" /> | `EXEC` | <CopyableCode code="organizationsId, resourceValueConfigsId" /> | Updates an existing ResourceValueConfigs with new rules. |
