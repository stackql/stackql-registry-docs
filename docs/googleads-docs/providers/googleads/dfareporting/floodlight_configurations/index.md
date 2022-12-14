---
title: floodlight_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - floodlight_configurations
  - dfareporting
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>floodlight_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.floodlight_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this floodlight configuration. This is a read-only, auto-generated field. |
| `firstDayOfWeek` | `string` | Day that will be counted as the first day of the week in reports. This is a required field. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#floodlightConfiguration". |
| `exposureToConversionEnabled` | `boolean` | Whether the exposure-to-conversion report is enabled. This report shows detailed pathway information on up to 10 of the most recent ad exposures seen by a user before converting. |
| `lookbackConfiguration` | `object` | Lookback configuration settings. |
| `inAppAttributionTrackingEnabled` | `boolean` | Whether in-app attribution tracking is enabled. |
| `customViewabilityMetric` | `object` | Custom Viewability Metric |
| `advertiserId` | `string` | Advertiser ID of the parent advertiser of this floodlight configuration. |
| `userDefinedVariableConfigurations` | `array` | List of user defined variables enabled for this configuration. |
| `subaccountId` | `string` | Subaccount ID of this floodlight configuration. This is a read-only field that can be left blank. |
| `tagSettings` | `object` | Dynamic and Image Tag Settings. |
| `analyticsDataSharingEnabled` | `boolean` | Whether advertiser data is shared with Google Analytics. |
| `naturalSearchConversionAttributionOption` | `string` | Types of attribution options for natural search conversions. |
| `omnitureSettings` | `object` | Omniture Integration Settings. |
| `thirdPartyAuthenticationTokens` | `array` | List of third-party authentication tokens enabled for this configuration. |
| `idDimensionValue` | `object` | Represents a DimensionValue resource. |
| `advertiserIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `accountId` | `string` | Account ID of this floodlight configuration. This is a read-only field that can be left blank. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `floodlightConfigurations_get` | `SELECT` | `id, profileId` | Gets one floodlight configuration by ID. |
| `floodlightConfigurations_list` | `SELECT` | `profileId` | Retrieves a list of floodlight configurations, possibly filtered. |
| `floodlightConfigurations_patch` | `EXEC` | `id, profileId` | Updates an existing floodlight configuration. This method supports patch semantics. |
| `floodlightConfigurations_update` | `EXEC` | `profileId` | Updates an existing floodlight configuration. |
