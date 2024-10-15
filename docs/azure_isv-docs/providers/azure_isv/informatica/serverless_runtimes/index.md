---
title: serverless_runtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - serverless_runtimes
  - informatica
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

Creates, updates, deletes, gets or lists a <code>serverless_runtimes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serverless_runtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.informatica.serverless_runtimes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_serverless_runtimes', value: 'view', },
        { label: 'serverless_runtimes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="advanced_custom_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute_units" /> | `text` | field from the `properties` object |
| <CopyableCode code="execution_timeout" /> | `text` | field from the `properties` object |
| <CopyableCode code="organizationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="platform" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverlessRuntimeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverless_account_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverless_runtime_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverless_runtime_network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverless_runtime_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverless_runtime_user_context_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supplementary_file_location" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Serverless Runtime properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="organizationName, resourceGroupName, serverlessRuntimeName, subscriptionId" /> | Get a InformaticaServerlessRuntimeResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="organizationName, resourceGroupName, serverlessRuntimeName, subscriptionId" /> | Create a InformaticaServerlessRuntimeResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="organizationName, resourceGroupName, serverlessRuntimeName, subscriptionId" /> | Delete a InformaticaServerlessRuntimeResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="organizationName, resourceGroupName, serverlessRuntimeName, subscriptionId" /> | Update a InformaticaServerlessRuntimeResource |
| <CopyableCode code="check_dependencies" /> | `EXEC` | <CopyableCode code="organizationName, resourceGroupName, serverlessRuntimeName, subscriptionId" /> | Checks all dependencies for a serverless runtime resource |
| <CopyableCode code="serverless_resource_by_id" /> | `EXEC` | <CopyableCode code="organizationName, resourceGroupName, serverlessRuntimeName, subscriptionId" /> | Returns a serverless runtime resource by ID |
| <CopyableCode code="start_failed_serverless_runtime" /> | `EXEC` | <CopyableCode code="organizationName, resourceGroupName, serverlessRuntimeName, subscriptionId" /> | Starts a failed runtime resource |

## `SELECT` examples

Get a InformaticaServerlessRuntimeResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_serverless_runtimes', value: 'view', },
        { label: 'serverless_runtimes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
advanced_custom_properties,
application_type,
compute_units,
execution_timeout,
organizationName,
platform,
provisioning_state,
resourceGroupName,
serverlessRuntimeName,
serverless_account_location,
serverless_runtime_config,
serverless_runtime_network_profile,
serverless_runtime_tags,
serverless_runtime_user_context_properties,
subscriptionId,
supplementary_file_location
FROM azure_isv.informatica.vw_serverless_runtimes
WHERE organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverlessRuntimeName = '{{ serverlessRuntimeName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.informatica.serverless_runtimes
WHERE organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverlessRuntimeName = '{{ serverlessRuntimeName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>serverless_runtimes</code> resource.

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
INSERT INTO azure_isv.informatica.serverless_runtimes (
organizationName,
resourceGroupName,
serverlessRuntimeName,
subscriptionId,
properties
)
SELECT 
'{{ organizationName }}',
'{{ resourceGroupName }}',
'{{ serverlessRuntimeName }}',
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
        - name: description
          value: string
        - name: platform
          value: []
        - name: applicationType
          value: []
        - name: computeUnits
          value: string
        - name: executionTimeout
          value: string
        - name: serverlessAccountLocation
          value: string
        - name: serverlessRuntimeNetworkProfile
          value:
            - name: networkInterfaceConfiguration
              value:
                - name: vnetId
                  value: string
                - name: subnetId
                  value: string
                - name: vnetResourceGuid
                  value: string
        - name: advancedCustomProperties
          value:
            - - name: key
                value: string
              - name: value
                value: string
        - name: supplementaryFileLocation
          value: string
        - name: serverlessRuntimeConfig
          value:
            - name: cdiConfigProps
              value:
                - - name: engineName
                    value: string
                  - name: engineVersion
                    value: string
                  - name: applicationConfigs
                    value:
                      - - name: type
                          value: string
                        - name: name
                          value: string
                        - name: value
                          value: string
                        - name: platform
                          value: string
                        - name: customized
                          value: string
                        - name: defaultValue
                          value: string
            - name: cdieConfigProps
              value:
                - - name: engineName
                    value: string
                  - name: engineVersion
                    value: string
                  - name: applicationConfigs
                    value:
                      - - name: type
                          value: string
                        - name: name
                          value: string
                        - name: value
                          value: string
                        - name: platform
                          value: string
                        - name: customized
                          value: string
                        - name: defaultValue
                          value: string
        - name: serverlessRuntimeTags
          value:
            - - name: name
                value: string
              - name: value
                value: string
        - name: serverlessRuntimeUserContextProperties
          value:
            - name: userContextToken
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>serverless_runtimes</code> resource.

```sql
/*+ update */
UPDATE azure_isv.informatica.serverless_runtimes
SET 
properties = '{{ properties }}'
WHERE 
organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverlessRuntimeName = '{{ serverlessRuntimeName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>serverless_runtimes</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.informatica.serverless_runtimes
WHERE organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverlessRuntimeName = '{{ serverlessRuntimeName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
