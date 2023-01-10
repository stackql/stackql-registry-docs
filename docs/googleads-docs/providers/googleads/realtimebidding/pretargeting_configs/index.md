---
title: pretargeting_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - pretargeting_configs
  - realtimebidding
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
<tr><td><b>Name</b></td><td><code>pretargeting_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.realtimebidding.pretargeting_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the pretargeting configuration that must follow the pattern `bidders/&#123;bidder_account_id&#125;/pretargetingConfigs/&#123;config_id&#125;` |
| `includedFormats` | `array` | Creative formats included by this configuration. Only bid requests eligible for at least one of the specified creative formats will be sent. An unset value will allow all bid requests to be sent, regardless of format. |
| `maximumQps` | `string` | The maximum QPS threshold for this configuration. The bidder should receive no more than this number of bid requests matching this configuration per second across all their bidding endpoints among all trading locations. Further information available at https://developers.google.com/authorized-buyers/rtb/peer-guide |
| `minimumViewabilityDecile` | `integer` | The targeted minimum viewability decile, ranging in values [0, 10]. A value of 5 means that the configuration will only match adslots for which we predict at least 50% viewability. Values &gt; 10 will be rounded down to 10. An unset value or a value of 0 indicates that bid requests will be sent regardless of viewability. |
| `verticalTargeting` | `object` | Generic targeting used for targeting dimensions that contain a list of included and excluded numeric IDs used in app, user list, geo, and vertical id targeting. |
| `publisherTargeting` | `object` | Generic targeting with string values used in app, website and publisher targeting. |
| `allowedUserTargetingModes` | `array` | Targeting modes included by this configuration. A bid request must allow all the specified targeting modes. An unset value allows all bid requests to be sent, regardless of which targeting modes they allow. |
| `includedPlatforms` | `array` | The platforms included by this configration. Bid requests for devices with the specified platform types will be sent. An unset value allows all bid requests to be sent, regardless of platform. |
| `webTargeting` | `object` | Generic targeting with string values used in app, website and publisher targeting. |
| `excludedContentLabelIds` | `array` | The sensitive content category label IDs excluded in this configuration. Bid requests for inventory with any of the specified content label IDs will not be sent. Refer to this file https://storage.googleapis.com/adx-rtb-dictionaries/content-labels.txt for category IDs. |
| `includedEnvironments` | `array` | Environments that are being included. Bid requests will not be sent for a given environment if it is not included. Further restrictions can be applied to included environments to target only a subset of its inventory. An unset value includes all environments. |
| `includedLanguages` | `array` | The languages included in this configuration, represented by their language code. See https://developers.google.com/adwords/api/docs/appendix/languagecodes. |
| `displayName` | `string` | The diplay name associated with this configuration. This name must be unique among all the pretargeting configurations a bidder has. |
| `userListTargeting` | `object` | Generic targeting used for targeting dimensions that contain a list of included and excluded numeric IDs used in app, user list, geo, and vertical id targeting. |
| `invalidGeoIds` | `array` | Output only. Existing included or excluded geos that are invalid. Previously targeted geos may become invalid due to privacy restrictions. |
| `interstitialTargeting` | `string` | The interstitial targeting specified for this configuration. The unset value will allow bid requests to be sent regardless of whether they are for interstitials or not. |
| `appTargeting` | `object` | A subset of app inventory to target. Bid requests that match criteria in at least one of the specified dimensions will be sent. |
| `includedUserIdTypes` | `array` | User identifier types included in this configuration. At least one of the user identifier types specified in this list must be available for the bid request to be sent. |
| `includedCreativeDimensions` | `array` | Creative dimensions included by this configuration. Only bid requests eligible for at least one of the specified creative dimensions will be sent. An unset value allows all bid requests to be sent, regardless of creative dimension. |
| `state` | `string` | Output only. The state of this pretargeting configuration. |
| `billingId` | `string` | Output only. The identifier that corresponds to this pretargeting configuration that helps buyers track and attribute their spend across their own arbitrary divisions. If a bid request matches more than one configuration, the buyer chooses which billing_id to attribute each of their bids. |
| `includedMobileOperatingSystemIds` | `array` | The mobile operating systems included in this configuration as defined in https://storage.googleapis.com/adx-rtb-dictionaries/mobile-os.csv |
| `geoTargeting` | `object` | Generic targeting used for targeting dimensions that contain a list of included and excluded numeric IDs used in app, user list, geo, and vertical id targeting. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bidders_pretargetingConfigs_get` | `SELECT` | `biddersId, pretargetingConfigsId` | Gets a pretargeting configuration. |
| `bidders_pretargetingConfigs_list` | `SELECT` | `biddersId` | Lists all pretargeting configurations for a single bidder. |
| `bidders_pretargetingConfigs_create` | `INSERT` | `biddersId` | Creates a pretargeting configuration. A pretargeting configuration's state (PretargetingConfig.state) is active upon creation, and it will start to affect traffic shortly after. A bidder may create a maximum of 10 pretargeting configurations. Attempts to exceed this maximum results in a 400 bad request error. |
| `bidders_pretargetingConfigs_delete` | `DELETE` | `biddersId, pretargetingConfigsId` | Deletes a pretargeting configuration. |
| `bidders_pretargetingConfigs_activate` | `EXEC` | `biddersId, pretargetingConfigsId` | Activates a pretargeting configuration. |
| `bidders_pretargetingConfigs_patch` | `EXEC` | `biddersId, pretargetingConfigsId` | Updates a pretargeting configuration. |
| `bidders_pretargetingConfigs_suspend` | `EXEC` | `biddersId, pretargetingConfigsId` | Suspends a pretargeting configuration. |
