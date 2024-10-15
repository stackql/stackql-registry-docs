---
title: organizations
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations
  - astro
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

Creates, updates, deletes, gets or lists a <code>organizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.astro.organizations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_organizations', value: 'view', },
        { label: 'organizations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="marketplace" /> | `text` | field from the `properties` object |
| <CopyableCode code="organizationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_organization_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="user" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties specific to Data Organization resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> | Get a OrganizationResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List OrganizationResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List OrganizationResource resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> | Create a OrganizationResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> | Delete a OrganizationResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> | Update a OrganizationResource |

## `SELECT` examples

List OrganizationResource resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_organizations', value: 'view', },
        { label: 'organizations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
identity,
location,
marketplace,
organizationName,
partner_organization_properties,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
user
FROM azure_isv.astro.vw_organizations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure_isv.astro.organizations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>organizations</code> resource.

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
INSERT INTO azure_isv.astro.organizations (
organizationName,
resourceGroupName,
subscriptionId,
properties,
identity,
tags,
location
)
SELECT 
'{{ organizationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: marketplace
          value:
            - name: subscriptionId
              value: string
            - name: subscriptionStatus
              value: []
            - name: offerDetails
              value:
                - name: publisherId
                  value: string
                - name: offerId
                  value: string
                - name: planId
                  value: string
                - name: planName
                  value: string
                - name: termUnit
                  value: string
                - name: termId
                  value: string
                - name: renewalMode
                  value: []
                - name: endDate
                  value: string
        - name: user
          value:
            - name: firstName
              value: string
            - name: lastName
              value: string
            - name: emailAddress
              value: []
            - name: upn
              value: string
            - name: phoneNumber
              value: string
        - name: provisioningState
          value: []
        - name: partnerOrganizationProperties
          value:
            - name: organizationId
              value: string
            - name: workspaceId
              value: string
            - name: organizationName
              value: string
            - name: workspaceName
              value: string
            - name: singleSignOnProperties
              value:
                - name: singleSignOnState
                  value: []
                - name: enterpriseAppId
                  value: string
                - name: singleSignOnUrl
                  value: []
                - name: aadDomains
                  value:
                    - string
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
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>organizations</code> resource.

```sql
/*+ update */
UPDATE azure_isv.astro.organizations
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>organizations</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.astro.organizations
WHERE organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
