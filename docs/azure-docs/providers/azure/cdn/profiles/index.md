---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - cdn
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

Creates, updates, deletes, gets or lists a <code>profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.profiles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_profiles', value: 'view', },
        { label: 'profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extended_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="front_door_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="kind" /> | `text` | Kind of the profile. Used by portal to differentiate traditional CDN profile and new AFD profile. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="log_scrubbing" /> | `text` | field from the `properties` object |
| <CopyableCode code="origin_response_timeout_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Standard_Verizon = The SKU name for a Standard Verizon CDN profile.
Premium_Verizon = The SKU name for a Premium Verizon CDN profile.
Custom_Verizon = The SKU name for a Custom Verizon CDN profile.
Standard_Akamai = The SKU name for an Akamai CDN profile.
Standard_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using GB based billing model.
Standard_Microsoft = The SKU name for a Standard Microsoft CDN profile.
Standard_AzureFrontDoor =  The SKU name for an Azure Front Door Standard profile.
Premium_AzureFrontDoor = The SKU name for an Azure Front Door Premium profile.
Standard_955BandWidth_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using 95-5 peak bandwidth billing model.
Standard_AvgBandWidth_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using monthly average peak bandwidth billing model.
StandardPlus_ChinaCdn = The SKU name for a China CDN profile for live-streaming using GB based billing model.
StandardPlus_955BandWidth_ChinaCdn = The SKU name for a China CDN live-streaming profile using 95-5 peak bandwidth billing model.
StandardPlus_AvgBandWidth_ChinaCdn = The SKU name for a China CDN live-streaming profile using monthly average peak bandwidth billing model.
 |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="kind" /> | `string` | Kind of the profile. Used by portal to differentiate traditional CDN profile and new AFD profile. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties required to create a profile. |
| <CopyableCode code="sku" /> | `object` | Standard_Verizon = The SKU name for a Standard Verizon CDN profile.
Premium_Verizon = The SKU name for a Premium Verizon CDN profile.
Custom_Verizon = The SKU name for a Custom Verizon CDN profile.
Standard_Akamai = The SKU name for an Akamai CDN profile.
Standard_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using GB based billing model.
Standard_Microsoft = The SKU name for a Standard Microsoft CDN profile.
Standard_AzureFrontDoor =  The SKU name for an Azure Front Door Standard profile.
Premium_AzureFrontDoor = The SKU name for an Azure Front Door Premium profile.
Standard_955BandWidth_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using 95-5 peak bandwidth billing model.
Standard_AvgBandWidth_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using monthly average peak bandwidth billing model.
StandardPlus_ChinaCdn = The SKU name for a China CDN profile for live-streaming using GB based billing model.
StandardPlus_955BandWidth_ChinaCdn = The SKU name for a China CDN live-streaming profile using 95-5 peak bandwidth billing model.
StandardPlus_AvgBandWidth_ChinaCdn = The SKU name for a China CDN live-streaming profile using monthly average peak bandwidth billing model.
 |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Gets an Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified profile name under the specified subscription and resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the Azure Front Door Standard, Azure Front Door Premium, and CDN profiles within an Azure subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the Azure Front Door Standard, Azure Front Door Premium, and CDN profiles within a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId, data__sku" /> | Creates a new Azure Front Door Standard or Azure Front Door Premium or CDN profile with a profile name under the specified subscription and resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Deletes an existing  Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified parameters. Deleting a profile will result in the deletion of all of the sub-resources including endpoints, origins and custom domains. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Updates an existing Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified profile name under the specified subscription and resource group. |
| <CopyableCode code="can_migrate" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, data__classicResourceReference" /> | Checks if CDN profile can be migrated to Azure Frontdoor(Standard/Premium) profile. |
| <CopyableCode code="generate_sso_uri" /> | `EXEC` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Generates a dynamic SSO URI used to sign in to the CDN supplemental portal. Supplemental portal is used to configure advanced feature capabilities that are not yet available in the Azure portal, such as core reports in a standard profile; rules engine, advanced HTTP reports, and real-time stats and alerts in a premium profile. The SSO URI changes approximately every 10 minutes. |
| <CopyableCode code="migrate" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, data__classicResourceReference, data__profileName, data__sku" /> | Migrate the CDN profile to Azure Frontdoor(Standard/Premium) profile. The change need to be committed after this. |
| <CopyableCode code="migration_commit" /> | `EXEC` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Commit the migrated Azure Frontdoor(Standard/Premium) profile. |

## `SELECT` examples

Lists all of the Azure Front Door Standard, Azure Front Door Premium, and CDN profiles within an Azure subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_profiles', value: 'view', },
        { label: 'profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
extended_properties,
front_door_id,
identity,
kind,
location,
log_scrubbing,
origin_response_timeout_seconds,
profileName,
provisioning_state,
resourceGroupName,
resource_state,
sku,
subscriptionId,
tags
FROM azure.cdn.vw_profiles
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
kind,
location,
properties,
sku,
tags
FROM azure.cdn.profiles
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>profiles</code> resource.

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
INSERT INTO azure.cdn.profiles (
profileName,
resourceGroupName,
subscriptionId,
data__sku,
location,
tags,
sku,
identity,
properties
)
SELECT 
'{{ profileName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__sku }}',
'{{ location }}',
'{{ tags }}',
'{{ sku }}',
'{{ identity }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: sku
      value:
        - name: name
          value: string
    - name: kind
      value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: properties
      value:
        - name: resourceState
          value: string
        - name: provisioningState
          value: string
        - name: extendedProperties
          value: object
        - name: frontDoorId
          value: string
        - name: originResponseTimeoutSeconds
          value: integer
        - name: logScrubbing
          value:
            - name: state
              value: string
            - name: scrubbingRules
              value:
                - - name: matchVariable
                    value: string
                  - name: selectorMatchOperator
                    value: string
                  - name: selector
                    value: string
                  - name: state
                    value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>profiles</code> resource.

```sql
/*+ update */
UPDATE azure.cdn.profiles
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>profiles</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cdn.profiles
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
