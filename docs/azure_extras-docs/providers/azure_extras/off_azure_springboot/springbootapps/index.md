---
title: springbootapps
hide_title: false
hide_table_of_contents: false
keywords:
  - springbootapps
  - off_azure_springboot
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

Creates, updates, deletes, gets or lists a <code>springbootapps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>springbootapps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.off_azure_springboot.springbootapps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_springbootapps', value: 'view', },
        { label: 'springbootapps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="app_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="app_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="app_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="artifact_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="binding_ports" /> | `text` | field from the `properties` object |
| <CopyableCode code="build_jdk_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificates" /> | `text` | field from the `properties` object |
| <CopyableCode code="checksum" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_strings" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependencies" /> | `text` | field from the `properties` object |
| <CopyableCode code="environments" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="instances" /> | `text` | field from the `properties` object |
| <CopyableCode code="jar_file_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="jvm_memory_in_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="jvm_options" /> | `text` | field from the `properties` object |
| <CopyableCode code="labels" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_updated_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_arm_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="miscs" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="runtime_jdk_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="servers" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="spring_boot_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="springbootappsName" /> | `text` | field from the `properties` object |
| <CopyableCode code="static_content_locations" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The springbootapps resource definition. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, springbootappsName, subscriptionId" /> | Get a springbootapps resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | List springbootapps resource by resourceGroup |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="siteName, subscriptionId" /> | List springbootapps resource by subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, siteName, springbootappsName, subscriptionId" /> | Create a springbootapps resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, siteName, springbootappsName, subscriptionId" /> | Delete a springbootapps resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, siteName, springbootappsName, subscriptionId" /> | Update a springbootapps resource. |

## `SELECT` examples

List springbootapps resource by subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_springbootapps', value: 'view', },
        { label: 'springbootapps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
app_name,
app_port,
app_type,
application_configurations,
artifact_name,
binding_ports,
build_jdk_version,
certificates,
checksum,
connection_strings,
dependencies,
environments,
errors,
instance_count,
instances,
jar_file_location,
jvm_memory_in_mb,
jvm_options,
labels,
last_modified_time,
last_updated_time,
machine_arm_ids,
miscs,
provisioning_state,
resourceGroupName,
runtime_jdk_version,
servers,
siteName,
spring_boot_version,
springbootappsName,
static_content_locations,
subscriptionId
FROM azure_extras.off_azure_springboot.vw_springbootapps
WHERE siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.off_azure_springboot.springbootapps
WHERE siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>springbootapps</code> resource.

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
INSERT INTO azure_extras.off_azure_springboot.springbootapps (
resourceGroupName,
siteName,
springbootappsName,
subscriptionId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ siteName }}',
'{{ springbootappsName }}',
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
        - name: appName
          value: string
        - name: artifactName
          value: string
        - name: appPort
          value: integer
        - name: appType
          value: string
        - name: applicationConfigurations
          value:
            - - name: key
                value: string
              - name: value
                value: string
        - name: bindingPorts
          value:
            - integer
        - name: buildJdkVersion
          value: string
        - name: certificates
          value:
            - string
        - name: checksum
          value: string
        - name: dependencies
          value:
            - string
        - name: environments
          value:
            - string
        - name: instanceCount
          value: integer
        - name: jarFileLocation
          value: string
        - name: jvmMemoryInMB
          value: integer
        - name: jvmOptions
          value:
            - string
        - name: miscs
          value:
            - - name: key
                value: string
              - name: value
                value: string
        - name: instances
          value:
            - - name: machineArmId
                value: string
              - name: instanceCount
                value: integer
              - name: jvmMemoryInMB
                value: integer
        - name: runtimeJdkVersion
          value: string
        - name: servers
          value:
            - string
        - name: machineArmIds
          value:
            - string
        - name: springBootVersion
          value: string
        - name: staticContentLocations
          value:
            - string
        - name: connectionStrings
          value:
            - string
        - name: lastModifiedTime
          value: string
        - name: lastUpdatedTime
          value: string
        - name: provisioningState
          value: string
        - name: errors
          value:
            - - name: id
                value: integer
              - name: code
                value: string
              - name: summaryMessage
                value: string
              - name: runAsAccountId
                value: string
              - name: message
                value: string
              - name: possibleCauses
                value: string
              - name: recommendedAction
                value: string
              - name: severity
                value: string
              - name: updatedTimeStamp
                value: string
        - name: labels
          value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>springbootapps</code> resource.

```sql
/*+ update */
UPDATE azure_extras.off_azure_springboot.springbootapps
SET 
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND springbootappsName = '{{ springbootappsName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>springbootapps</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.off_azure_springboot.springbootapps
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND springbootappsName = '{{ springbootappsName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
