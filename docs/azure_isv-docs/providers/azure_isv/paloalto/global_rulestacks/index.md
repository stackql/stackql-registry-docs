---
title: global_rulestacks
hide_title: false
hide_table_of_contents: false
keywords:
  - global_rulestacks
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

Creates, updates, deletes, gets or lists a <code>global_rulestacks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_rulestacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.global_rulestacks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_global_rulestacks', value: 'view', },
        { label: 'global_rulestacks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="associated_subscriptions" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="globalRulestackName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | The properties of the managed service identities assigned to this resource. |
| <CopyableCode code="location" /> | `text` | Global Location |
| <CopyableCode code="min_app_id_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="pan_etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="pan_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_services" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | The properties of the managed service identities assigned to this resource. |
| <CopyableCode code="location" /> | `string` | Global Location |
| <CopyableCode code="properties" /> | `object` | PAN Rulestack Describe Object |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="globalRulestackName" /> | Get a GlobalRulestackResource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | List GlobalRulestackResource resources by Tenant |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="globalRulestackName, data__location, data__properties" /> | Create a GlobalRulestackResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="globalRulestackName" /> | Delete a GlobalRulestackResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="globalRulestackName" /> | Update a GlobalRulestackResource |
| <CopyableCode code="commit" /> | `EXEC` | <CopyableCode code="globalRulestackName" /> | Commit rulestack configuration |
| <CopyableCode code="revert" /> | `EXEC` | <CopyableCode code="globalRulestackName" /> | Revert rulestack configuration |

## `SELECT` examples

List GlobalRulestackResource resources by Tenant

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_global_rulestacks', value: 'view', },
        { label: 'global_rulestacks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
associated_subscriptions,
default_mode,
globalRulestackName,
identity,
location,
min_app_id_version,
pan_etag,
pan_location,
provisioning_state,
scope,
security_services,
system_data
FROM azure_isv.paloalto.vw_global_rulestacks
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
systemData
FROM azure_isv.paloalto.global_rulestacks
;
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>global_rulestacks</code> resource.

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
INSERT INTO azure_isv.paloalto.global_rulestacks (
globalRulestackName,
data__location,
data__properties,
properties,
location,
identity
)
SELECT 
'{{ globalRulestackName }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ location }}',
'{{ identity }}'
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
    - name: location
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>global_rulestacks</code> resource.

```sql
/*+ update */
UPDATE azure_isv.paloalto.global_rulestacks
SET 
location = '{{ location }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
globalRulestackName = '{{ globalRulestackName }}';
```

## `DELETE` example

Deletes the specified <code>global_rulestacks</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.paloalto.global_rulestacks
WHERE globalRulestackName = '{{ globalRulestackName }}';
```
