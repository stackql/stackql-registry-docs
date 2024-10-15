---
title: web_app_sites_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - web_app_sites_controllers
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

Creates, updates, deletes, gets or lists a <code>web_app_sites_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_app_sites_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.web_app_sites_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_web_app_sites_controllers', value: 'view', },
        { label: 'web_app_sites_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="discovery_scenario" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="site_appliance_properties_collection" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="webAppSiteName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class for Web app site properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | Method to get a site. |
| <CopyableCode code="list_by_master_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to get all sites. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | Method to create a WebApp site. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | Deletes the WebApp site. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | Method to update an existing site. |
| <CopyableCode code="error_summary" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | MMethod to get error summary from web app  site. |
| <CopyableCode code="export_inventory" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | Method to generate report containing web app inventory. |
| <CopyableCode code="refresh" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | Method to refresh a site. |
| <CopyableCode code="summary" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | Method to get site usage/summary. |

## `SELECT` examples

Method to get all sites.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_web_app_sites_controllers', value: 'view', },
        { label: 'web_app_sites_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
discovery_scenario,
provisioning_state,
resourceGroupName,
service_endpoint,
siteName,
site_appliance_properties_collection,
subscriptionId,
webAppSiteName
FROM azure.migrate.vw_web_app_sites_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.web_app_sites_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>web_app_sites_controllers</code> resource.

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
INSERT INTO azure.migrate.web_app_sites_controllers (
resourceGroupName,
siteName,
subscriptionId,
webAppSiteName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ siteName }}',
'{{ subscriptionId }}',
'{{ webAppSiteName }}',
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
        - name: siteAppliancePropertiesCollection
          value:
            - - name: servicePrincipalIdentityDetails
                value:
                  - name: tenantId
                    value: string
                  - name: applicationId
                    value: string
                  - name: objectId
                    value: string
                  - name: audience
                    value: string
                  - name: aadAuthority
                    value: string
                  - name: rawCertData
                    value: string
              - name: agentDetails
                value:
                  - name: id
                    value: string
                  - name: version
                    value: string
                  - name: lastHeartBeatUtc
                    value: string
                  - name: keyVaultUri
                    value: string
                  - name: keyVaultId
                    value: string
              - name: applianceName
                value: string
        - name: discoveryScenario
          value: []
        - name: serviceEndpoint
          value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>web_app_sites_controllers</code> resource.

```sql
/*+ update */
UPDATE azure.migrate.web_app_sites_controllers
SET 
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND webAppSiteName = '{{ webAppSiteName }}';
```

## `DELETE` example

Deletes the specified <code>web_app_sites_controllers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.migrate.web_app_sites_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND webAppSiteName = '{{ webAppSiteName }}';
```
