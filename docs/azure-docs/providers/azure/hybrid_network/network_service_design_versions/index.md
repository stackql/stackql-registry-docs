---
title: network_service_design_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_service_design_versions
  - hybrid_network
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

Creates, updates, deletes, gets or lists a <code>network_service_design_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_service_design_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.network_service_design_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_service_design_versions', value: 'view', },
        { label: 'network_service_design_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_group_schema_references" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="networkServiceDesignGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkServiceDesignVersionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="nfvis_from_site" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisherName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_element_templates" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="version_state" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | network service design version properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkServiceDesignGroupName, networkServiceDesignVersionName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about a network service design version. |
| <CopyableCode code="list_by_network_service_design_group" /> | `SELECT` | <CopyableCode code="networkServiceDesignGroupName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about a list of network service design versions under a network service design group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkServiceDesignGroupName, networkServiceDesignVersionName, publisherName, resourceGroupName, subscriptionId" /> | Creates or updates a network service design version. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkServiceDesignGroupName, networkServiceDesignVersionName, publisherName, resourceGroupName, subscriptionId" /> | Deletes the specified network service design version. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="networkServiceDesignGroupName, networkServiceDesignVersionName, publisherName, resourceGroupName, subscriptionId" /> | Updates a network service design version resource. |
| <CopyableCode code="update_state" /> | `EXEC` | <CopyableCode code="networkServiceDesignGroupName, networkServiceDesignVersionName, publisherName, resourceGroupName, subscriptionId" /> | Update network service design version state. |

## `SELECT` examples

Gets information about a list of network service design versions under a network service design group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_service_design_versions', value: 'view', },
        { label: 'network_service_design_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
configuration_group_schema_references,
location,
networkServiceDesignGroupName,
networkServiceDesignVersionName,
nfvis_from_site,
provisioning_state,
publisherName,
resourceGroupName,
resource_element_templates,
subscriptionId,
tags,
version_state
FROM azure.hybrid_network.vw_network_service_design_versions
WHERE networkServiceDesignGroupName = '{{ networkServiceDesignGroupName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.hybrid_network.network_service_design_versions
WHERE networkServiceDesignGroupName = '{{ networkServiceDesignGroupName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_service_design_versions</code> resource.

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
INSERT INTO azure.hybrid_network.network_service_design_versions (
networkServiceDesignGroupName,
networkServiceDesignVersionName,
publisherName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ networkServiceDesignGroupName }}',
'{{ networkServiceDesignVersionName }}',
'{{ publisherName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: versionState
          value: []
        - name: description
          value: string
        - name: configurationGroupSchemaReferences
          value: object
        - name: nfvisFromSite
          value: object
        - name: resourceElementTemplates
          value:
            - - name: name
                value: string
              - name: type
                value: []
              - name: dependsOnProfile
                value:
                  - name: installDependsOn
                    value:
                      - string
                  - name: uninstallDependsOn
                    value:
                      - string
                  - name: updateDependsOn
                    value:
                      - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>network_service_design_versions</code> resource.

```sql
/*+ update */
UPDATE azure.hybrid_network.network_service_design_versions
SET 
tags = '{{ tags }}'
WHERE 
networkServiceDesignGroupName = '{{ networkServiceDesignGroupName }}'
AND networkServiceDesignVersionName = '{{ networkServiceDesignVersionName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>network_service_design_versions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_network.network_service_design_versions
WHERE networkServiceDesignGroupName = '{{ networkServiceDesignGroupName }}'
AND networkServiceDesignVersionName = '{{ networkServiceDesignVersionName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
