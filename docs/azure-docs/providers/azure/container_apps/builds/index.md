---
title: builds
hide_title: false
hide_table_of_contents: false
keywords:
  - builds
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>builds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>builds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.builds" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_builds', value: 'view', },
        { label: 'builds', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="buildName" /> | `text` | field from the `properties` object |
| <CopyableCode code="build_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="builderName" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination_container_registry" /> | `text` | field from the `properties` object |
| <CopyableCode code="log_stream_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="token_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="upload_endpoint" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The build properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="buildName, builderName, resourceGroupName, subscriptionId" /> | Get a BuildResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="buildName, builderName, resourceGroupName, subscriptionId" /> | Create a BuildResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="buildName, builderName, resourceGroupName, subscriptionId" /> | Delete a BuildResource |

## `SELECT` examples

Get a BuildResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_builds', value: 'view', },
        { label: 'builds', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
buildName,
build_status,
builderName,
configuration,
destination_container_registry,
log_stream_endpoint,
provisioning_state,
resourceGroupName,
subscriptionId,
token_endpoint,
upload_endpoint
FROM azure.container_apps.vw_builds
WHERE buildName = '{{ buildName }}'
AND builderName = '{{ builderName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.container_apps.builds
WHERE buildName = '{{ buildName }}'
AND builderName = '{{ builderName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>builds</code> resource.

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
INSERT INTO azure.container_apps.builds (
buildName,
builderName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ buildName }}',
'{{ builderName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: buildStatus
          value: []
        - name: destinationContainerRegistry
          value:
            - name: server
              value: string
            - name: image
              value: string
        - name: configuration
          value:
            - name: baseOs
              value: string
            - name: platform
              value: string
            - name: platformVersion
              value: string
            - name: environmentVariables
              value:
                - - name: name
                    value: string
                  - name: value
                    value: string
            - name: preBuildSteps
              value:
                - - name: description
                    value: string
                  - name: scripts
                    value:
                      - string
                  - name: httpGet
                    value:
                      - name: url
                        value: string
                      - name: fileName
                        value: string
                      - name: headers
                        value:
                          - string
        - name: uploadEndpoint
          value: string
        - name: logStreamEndpoint
          value: string
        - name: tokenEndpoint
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>builds</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.builds
WHERE buildName = '{{ buildName }}'
AND builderName = '{{ builderName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
