---
title: tomcat_web_servers_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - tomcat_web_servers_controllers
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

Creates, updates, deletes, gets or lists a <code>tomcat_web_servers_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tomcat_web_servers_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.tomcat_web_servers_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tomcat_web_servers_controllers', value: 'view', },
        { label: 'tomcat_web_servers_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="appliance_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="catalina_home" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="has_errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_access_log_valve_present" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_clustering_present" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_deleted" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_memory_realm_present" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_session_tracking_present" /> | `text` | field from the `properties` object |
| <CopyableCode code="jvm_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_memory_usage_in_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="operating_system_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_as_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="services" /> | `text` | field from the `properties` object |
| <CopyableCode code="session_persistence_mechanism" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="webAppSiteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="webServerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="web_applications" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class for web server properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName, webServerName" /> | Method to get an Tomcat web server. |
| <CopyableCode code="list_by_web_app_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | Method to get all Tomcat web servers. |

## `SELECT` examples

Method to get all Tomcat web servers.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tomcat_web_servers_controllers', value: 'view', },
        { label: 'tomcat_web_servers_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
appliance_names,
catalina_home,
configuration_location,
created_timestamp,
display_name,
errors,
has_errors,
is_access_log_valve_present,
is_clustering_present,
is_deleted,
is_memory_realm_present,
is_session_tracking_present,
jvm_version,
machine_ids,
max_memory_usage_in_mb,
operating_system_details,
provisioning_state,
resourceGroupName,
run_as_account_id,
server_fqdn,
server_type,
services,
session_persistence_mechanism,
siteName,
subscriptionId,
updated_timestamp,
version,
webAppSiteName,
webServerName,
web_applications
FROM azure.migrate.vw_tomcat_web_servers_controllers
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
FROM azure.migrate.tomcat_web_servers_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND webAppSiteName = '{{ webAppSiteName }}';
```
</TabItem></Tabs>

