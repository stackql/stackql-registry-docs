---
title: site_network_services
hide_title: false
hide_table_of_contents: false
keywords:
  - site_network_services
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

Creates, updates, deletes, gets or lists a <code>site_network_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>site_network_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.site_network_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_site_network_services', value: 'view', },
        { label: 'site_network_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="desired_state_configuration_group_value_references" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="last_state_configuration_group_value_references" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_state_network_service_design_version_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="managed_resource_group_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_service_design_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_service_design_version_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_service_design_version_offering_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_service_design_version_resource_reference" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteNetworkServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="site_reference" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Sku, to be associated with a SiteNetworkService. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Site network service properties. |
| <CopyableCode code="sku" /> | `object` | Sku, to be associated with a SiteNetworkService. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteNetworkServiceName, subscriptionId" /> | Gets information about the specified site network service. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all site network services. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all sites in the network service in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, siteNetworkServiceName, subscriptionId" /> | Creates or updates a network site. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, siteNetworkServiceName, subscriptionId" /> | Deletes the specified site network service. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteNetworkServiceName, subscriptionId" /> | Updates a site update tags. |

## `SELECT` examples

Lists all sites in the network service in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_site_network_services', value: 'view', },
        { label: 'site_network_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
desired_state_configuration_group_value_references,
identity,
last_state_configuration_group_value_references,
last_state_network_service_design_version_name,
location,
managed_resource_group_configuration,
network_service_design_group_name,
network_service_design_version_name,
network_service_design_version_offering_location,
network_service_design_version_resource_reference,
provisioning_state,
publisher_name,
publisher_scope,
resourceGroupName,
siteNetworkServiceName,
site_reference,
sku,
subscriptionId,
tags
FROM azure.hybrid_network.vw_site_network_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
sku,
tags
FROM azure.hybrid_network.site_network_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>site_network_services</code> resource.

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
INSERT INTO azure.hybrid_network.site_network_services (
resourceGroupName,
siteNetworkServiceName,
subscriptionId,
properties,
identity,
sku,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ siteNetworkServiceName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
'{{ sku }}',
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
        - name: provisioningState
          value: []
        - name: managedResourceGroupConfiguration
          value:
            - name: name
              value: string
            - name: location
              value: string
        - name: siteReference
          value:
            - name: id
              value: string
        - name: publisherName
          value: string
        - name: publisherScope
          value: []
        - name: networkServiceDesignGroupName
          value: string
        - name: networkServiceDesignVersionName
          value: string
        - name: networkServiceDesignVersionOfferingLocation
          value: string
        - name: networkServiceDesignVersionResourceReference
          value:
            - name: idType
              value: []
        - name: desiredStateConfigurationGroupValueReferences
          value: object
        - name: lastStateNetworkServiceDesignVersionName
          value: string
        - name: lastStateConfigurationGroupValueReferences
          value: object
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
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>site_network_services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_network.site_network_services
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteNetworkServiceName = '{{ siteNetworkServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
