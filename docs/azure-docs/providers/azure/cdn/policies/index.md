---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
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

Creates, updates, deletes, gets or lists a <code>policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_policies', value: 'view', },
        { label: 'policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="custom_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint_links" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Gets a unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extended_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="managed_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="policyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="rate_limit_rules" /> | `text` | field from the `properties` object |
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
StandardPlus_AvgBandWidth_ChinaCdn = The SKU name for a China CDN live-streaming profile using monthly average peak bandwidth billing model. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Gets a unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Defines CDN web application firewall policy properties. |
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
StandardPlus_AvgBandWidth_ChinaCdn = The SKU name for a China CDN live-streaming profile using monthly average peak bandwidth billing model. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Retrieve protection policy with specified name within a resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the protection policies within a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="policyName, resourceGroupName, subscriptionId, data__sku" /> | Create or update policy with specified rule set name within a resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Deletes Policy |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Update an existing CdnWebApplicationFirewallPolicy with the specified policy name under the specified subscription and resource group |

## `SELECT` examples

Lists all of the protection policies within a resource group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_policies', value: 'view', },
        { label: 'policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
custom_rules,
endpoint_links,
etag,
extended_properties,
location,
managed_rules,
policyName,
policy_settings,
provisioning_state,
rate_limit_rules,
resourceGroupName,
resource_state,
sku,
subscriptionId,
tags
FROM azure.cdn.vw_policies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
sku,
tags
FROM azure.cdn.policies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policies</code> resource.

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
INSERT INTO azure.cdn.policies (
policyName,
resourceGroupName,
subscriptionId,
data__sku,
properties,
etag,
sku,
location,
tags
)
SELECT 
'{{ policyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__sku }}',
'{{ properties }}',
'{{ etag }}',
'{{ sku }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: policySettings
          value:
            - name: enabledState
              value: string
            - name: mode
              value: string
            - name: defaultRedirectUrl
              value: string
            - name: defaultCustomBlockResponseStatusCode
              value: integer
            - name: defaultCustomBlockResponseBody
              value: string
        - name: rateLimitRules
          value:
            - name: rules
              value:
                - - name: rateLimitThreshold
                    value: integer
                  - name: rateLimitDurationInMinutes
                    value: integer
                  - name: name
                    value: string
                  - name: enabledState
                    value: string
                  - name: priority
                    value: integer
                  - name: matchConditions
                    value:
                      - - name: matchVariable
                          value: string
                        - name: selector
                          value: string
                        - name: operator
                          value: string
                        - name: negateCondition
                          value: boolean
                        - name: matchValue
                          value:
                            - string
                        - name: transforms
                          value:
                            - []
                  - name: action
                    value: []
        - name: customRules
          value:
            - name: rules
              value:
                - - name: name
                    value: string
                  - name: enabledState
                    value: string
                  - name: priority
                    value: integer
                  - name: matchConditions
                    value:
                      - - name: matchVariable
                          value: string
                        - name: selector
                          value: string
                        - name: operator
                          value: string
                        - name: negateCondition
                          value: boolean
                        - name: matchValue
                          value:
                            - string
                        - name: transforms
                          value:
                            - []
        - name: managedRules
          value:
            - name: managedRuleSets
              value:
                - - name: ruleSetType
                    value: string
                  - name: ruleSetVersion
                    value: string
                  - name: anomalyScore
                    value: integer
                  - name: ruleGroupOverrides
                    value:
                      - - name: ruleGroupName
                          value: string
                        - name: rules
                          value:
                            - - name: ruleId
                                value: string
                              - name: enabledState
                                value: string
        - name: endpointLinks
          value:
            - - name: id
                value: string
        - name: extendedProperties
          value: object
        - name: provisioningState
          value: string
        - name: resourceState
          value: string
    - name: etag
      value: string
    - name: sku
      value:
        - name: name
          value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>policies</code> resource.

```sql
/*+ update */
UPDATE azure.cdn.policies
SET 
tags = '{{ tags }}'
WHERE 
policyName = '{{ policyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cdn.policies
WHERE policyName = '{{ policyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
