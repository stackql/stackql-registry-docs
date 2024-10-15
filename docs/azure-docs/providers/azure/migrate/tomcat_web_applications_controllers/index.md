---
title: tomcat_web_applications_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - tomcat_web_applications_controllers
  - migrate
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

Creates, updates, deletes, gets or lists a <code>tomcat_web_applications_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tomcat_web_applications_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.tomcat_web_applications_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tomcat_web_applications_controllers', value: 'view', },
        { label: 'tomcat_web_applications_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="appliance_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="bindings" /> | `text` | field from the `properties` object |
| <CopyableCode code="configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="directories" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="frameworks" /> | `text` | field from the `properties` object |
| <CopyableCode code="has_database_dependency" /> | `text` | field from the `properties` object |
| <CopyableCode code="has_errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_deleted" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_external_logging_configured" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_arm_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="physical_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="static_folders" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="webAppSiteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="webApplicationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="web_server_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="web_server_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class for web application properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName, webApplicationName" /> | Method to get an Tomcat web application. |
| <CopyableCode code="list_by_web_app_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | Method to get all Tomcat web application. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName, webApplicationName" /> | Updates the Tomcat web application tags. |

## `SELECT` examples

Method to get all Tomcat web application.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tomcat_web_applications_controllers', value: 'view', },
        { label: 'tomcat_web_applications_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
appliance_names,
bindings,
configurations,
created_timestamp,
directories,
display_name,
errors,
frameworks,
has_database_dependency,
has_errors,
is_deleted,
is_external_logging_configured,
machine_arm_ids,
machine_display_name,
physical_path,
provisioning_state,
resourceGroupName,
server_type,
siteName,
static_folders,
subscriptionId,
tags,
updated_timestamp,
virtual_path,
webAppSiteName,
webApplicationName,
web_server_id,
web_server_name
FROM azure.migrate.vw_tomcat_web_applications_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND webAppSiteName = '{{ webAppSiteName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.tomcat_web_applications_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND webAppSiteName = '{{ webAppSiteName }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>tomcat_web_applications_controllers</code> resource.

```sql
/*+ update */
UPDATE azure.migrate.tomcat_web_applications_controllers
SET 

WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND webAppSiteName = '{{ webAppSiteName }}'
AND webApplicationName = '{{ webApplicationName }}';
```
