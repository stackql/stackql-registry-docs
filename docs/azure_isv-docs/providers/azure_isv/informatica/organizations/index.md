---
title: organizations
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations
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

Creates, updates, deletes, gets or lists a <code>organizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.informatica.organizations" /></td></tr>
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
| <CopyableCode code="company_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="informatica_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="link_organization" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="marketplace_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="organizationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="user_details" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties specific to the Informatica DataManagement Organization resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> | Get a InformaticaOrganizationResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List InformaticaOrganizationResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List InformaticaOrganizationResource resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> | Create a InformaticaOrganizationResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> | Delete a InformaticaOrganizationResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> | Update a InformaticaOrganizationResource |

## `SELECT` examples

List InformaticaOrganizationResource resources by subscription ID

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
company_details,
informatica_properties,
link_organization,
location,
marketplace_details,
organizationName,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
user_details
FROM azure_isv.informatica.vw_organizations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure_isv.informatica.organizations
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
INSERT INTO azure_isv.informatica.organizations (
organizationName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ organizationName }}',
'{{ resourceGroupName }}',
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
        - name: provisioningState
          value: []
        - name: informaticaProperties
          value:
            - name: organizationId
              value: string
            - name: organizationName
              value: string
            - name: informaticaRegion
              value: string
            - name: singleSignOnUrl
              value: string
        - name: marketplaceDetails
          value:
            - name: marketplaceSubscriptionId
              value: string
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
        - name: userDetails
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
        - name: companyDetails
          value:
            - name: companyName
              value: string
            - name: officeAddress
              value: string
            - name: country
              value: string
            - name: domain
              value: string
            - name: business
              value: string
            - name: numberOfEmployees
              value: integer
        - name: linkOrganization
          value:
            - name: token
              value: string
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
UPDATE azure_isv.informatica.organizations
SET 
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
DELETE FROM azure_isv.informatica.organizations
WHERE organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
