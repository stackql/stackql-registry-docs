---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - app_service
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

Creates, updates, deletes, gets or lists a <code>domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | Domain resource specific properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Description for Get a domain. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for Get all domains in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for Get all domains in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Description for Creates or updates a domain. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Description for Delete a domain. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Description for Creates or updates a domain. |
| <CopyableCode code="check_availability" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Description for Check if a domain is available for registration. |
| <CopyableCode code="renew" /> | `EXEC` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Description for Renew a domain. |
| <CopyableCode code="transfer_out" /> | `EXEC` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples

Description for Get all domains in a subscription.


```sql
SELECT
id,
name,
kind,
location,
properties,
tags,
type
FROM azure.app_service.domains
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>domains</code> resource.

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
INSERT INTO azure.app_service.domains (
domainName,
resourceGroupName,
subscriptionId,
kind,
location,
tags,
properties
)
SELECT 
'{{ domainName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: location
      value: string
    - name: type
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: contactAdmin
          value:
            - name: addressMailing
              value:
                - name: address1
                  value: string
                - name: address2
                  value: string
                - name: city
                  value: string
                - name: country
                  value: string
                - name: postalCode
                  value: string
                - name: state
                  value: string
            - name: email
              value: string
            - name: fax
              value: string
            - name: jobTitle
              value: string
            - name: nameFirst
              value: string
            - name: nameLast
              value: string
            - name: nameMiddle
              value: string
            - name: organization
              value: string
            - name: phone
              value: string
        - name: registrationStatus
          value: string
        - name: provisioningState
          value: string
        - name: nameServers
          value:
            - string
        - name: privacy
          value: boolean
        - name: createdTime
          value: string
        - name: expirationTime
          value: string
        - name: lastRenewedTime
          value: string
        - name: autoRenew
          value: boolean
        - name: readyForDnsRecordManagement
          value: boolean
        - name: managedHostNames
          value:
            - - name: name
                value: string
              - name: siteNames
                value:
                  - string
              - name: azureResourceName
                value: string
              - name: azureResourceType
                value: string
              - name: customHostNameDnsRecordType
                value: string
              - name: hostNameType
                value: string
        - name: consent
          value:
            - name: agreementKeys
              value:
                - string
            - name: agreedBy
              value: string
            - name: agreedAt
              value: string
        - name: domainNotRenewableReasons
          value:
            - string
        - name: dnsType
          value: string
        - name: dnsZoneId
          value: string
        - name: targetDnsType
          value: string
        - name: authCode
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>domains</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.domains
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
domainName = '{{ domainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>domains</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.domains
WHERE domainName = '{{ domainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
