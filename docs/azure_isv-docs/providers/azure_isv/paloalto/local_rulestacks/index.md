---
title: local_rulestacks
hide_title: false
hide_table_of_contents: false
keywords:
  - local_rulestacks
  - paloalto
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

Creates, updates, deletes, gets or lists a <code>local_rulestacks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_rulestacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.local_rulestacks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_local_rulestacks', value: 'view', },
        { label: 'local_rulestacks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="associated_subscriptions" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | The properties of the managed service identities assigned to this resource. |
| <CopyableCode code="localRulestackName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="min_app_id_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="pan_etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="pan_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_services" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | The properties of the managed service identities assigned to this resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | PAN Rulestack Describe Object |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | Get a LocalRulestackResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List LocalRulestackResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List LocalRulestackResource resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId, data__properties" /> | Create a LocalRulestackResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | Delete a LocalRulestackResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | Update a LocalRulestackResource |
| <CopyableCode code="commit" /> | `EXEC` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | Commit rulestack configuration |
| <CopyableCode code="revert" /> | `EXEC` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | Revert rulestack configuration |

## `SELECT` examples

List LocalRulestackResource resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_local_rulestacks', value: 'view', },
        { label: 'local_rulestacks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
associated_subscriptions,
default_mode,
identity,
localRulestackName,
location,
min_app_id_version,
pan_etag,
pan_location,
provisioning_state,
resourceGroupName,
scope,
security_services,
subscriptionId,
system_data,
tags
FROM azure_isv.paloalto.vw_local_rulestacks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
systemData,
tags
FROM azure_isv.paloalto.local_rulestacks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>local_rulestacks</code> resource.

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
INSERT INTO azure_isv.paloalto.local_rulestacks (
localRulestackName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
identity,
tags,
location
)
SELECT 
'{{ localRulestackName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ identity }}',
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
        - name: panEtag
          value: string
        - name: panLocation
          value: string
        - name: scope
          value: []
        - name: associatedSubscriptions
          value:
            - string
        - name: description
          value: string
        - name: defaultMode
          value: []
        - name: minAppIdVersion
          value: string
        - name: provisioningState
          value: []
        - name: securityServices
          value:
            - name: vulnerabilityProfile
              value: string
            - name: antiSpywareProfile
              value: string
            - name: antiVirusProfile
              value: string
            - name: urlFilteringProfile
              value: string
            - name: fileBlockingProfile
              value: string
            - name: dnsSubscription
              value: string
            - name: outboundUnTrustCertificate
              value: string
            - name: outboundTrustCertificate
              value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: identity
      value:
        - name: tenantId
          value: string
        - name: principalId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: object
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>local_rulestacks</code> resource.

```sql
/*+ update */
UPDATE azure_isv.paloalto.local_rulestacks
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
localRulestackName = '{{ localRulestackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>local_rulestacks</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.paloalto.local_rulestacks
WHERE localRulestackName = '{{ localRulestackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
