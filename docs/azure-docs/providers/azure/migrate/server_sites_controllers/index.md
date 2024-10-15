---
title: server_sites_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - server_sites_controllers
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

Creates, updates, deletes, gets or lists a <code>server_sites_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_sites_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.server_sites_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_sites_controllers', value: 'view', },
        { label: 'server_sites_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="agent_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="appliance_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="discovery_solution_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="master_site_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_principal_identity_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of SiteResource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Get a ServerSiteResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List ServerSiteResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List ServerSiteResource resources by subscription ID |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Create a ServerSiteResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Delete a ServerSiteResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Update a ServerSiteResource |
| <CopyableCode code="compute_error_summary" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Get the error summary for a server site. |
| <CopyableCode code="computeusage" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Get a serve site usage. |
| <CopyableCode code="export_applications" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to generate report containing
            machine and the deep discovery of the application installed in the machine. |
| <CopyableCode code="export_machine_errors" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to generate report containing 
            machine and the errors encountered during guest discovery of the machine. |
| <CopyableCode code="refresh_site" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Operation to refresh a site |
| <CopyableCode code="summary" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to get site usage. |

## `SELECT` examples

List ServerSiteResource resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_sites_controllers', value: 'view', },
        { label: 'server_sites_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
agent_details,
appliance_name,
discovery_solution_id,
location,
master_site_id,
provisioning_state,
resourceGroupName,
service_endpoint,
service_principal_identity_details,
siteName,
subscriptionId,
tags
FROM azure.migrate.vw_server_sites_controllers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.migrate.server_sites_controllers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>server_sites_controllers</code> resource.

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
INSERT INTO azure.migrate.server_sites_controllers (
resourceGroupName,
siteName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ siteName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: masterSiteId
          value: string
        - name: servicePrincipalIdentityDetails
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
        - name: discoverySolutionId
          value: string
        - name: serviceEndpoint
          value: string
        - name: provisioningState
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>server_sites_controllers</code> resource.

```sql
/*+ update */
UPDATE azure.migrate.server_sites_controllers
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>server_sites_controllers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.migrate.server_sites_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
