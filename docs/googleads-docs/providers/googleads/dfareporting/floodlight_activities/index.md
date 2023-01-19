---
title: floodlight_activities
hide_title: false
hide_table_of_contents: false
keywords:
  - floodlight_activities
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
<tr><td><b>Name</b></td><td><code>floodlight_activities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.floodlight_activities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this floodlight activity. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this floodlight activity. This is a required field. Must be less than 129 characters long and cannot contain quotes. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#floodlightActivity". |
| `notes` | `string` | General notes or implementation instructions for the tag. |
| `attributionEnabled` | `boolean` | Whether the activity is enabled for attribution. |
| `floodlightActivityGroupType` | `string` | Type of the associated floodlight activity group. This is a read-only field. |
| `floodlightActivityGroupName` | `string` | Name of the associated floodlight activity group. This is a read-only field. |
| `cacheBustingType` | `string` | Code type used for cache busting in the generated tag. Applicable only when floodlightActivityGroupType is COUNTER and countingMethod is STANDARD_COUNTING or UNIQUE_COUNTING. |
| `status` | `string` | The status of the activity. This can only be set to ACTIVE or ARCHIVED_AND_DISABLED. The ARCHIVED status is no longer supported and cannot be set for Floodlight activities. The DISABLED_POLICY status indicates that a Floodlight activity is violating Google policy. Contact your account manager for more information. |
| `floodlightActivityGroupTagString` | `string` | Tag string of the associated floodlight activity group. This is a read-only field. |
| `sslRequired` | `boolean` | Whether this floodlight activity must be SSL-compliant. |
| `countingMethod` | `string` | Counting method for conversions for this floodlight activity. This is a required field. |
| `tagString` | `string` | Value of the cat= parameter in the floodlight tag, which the ad servers use to identify the activity. This is optional: if empty, a new tag string will be generated for you. This string must be 1 to 8 characters long, with valid characters being a-z0-9[ _ ]. This tag string must also be unique among activities of the same activity group. This field is read-only after insertion. |
| `advertiserId` | `string` | Advertiser ID of this floodlight activity. If this field is left blank, the value will be copied over either from the activity group's advertiser or the existing activity's advertiser. |
| `publisherTags` | `array` | Publisher dynamic floodlight tags. |
| `advertiserIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `floodlightConfigurationIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `expectedUrl` | `string` | URL where this tag will be deployed. If specified, must be less than 256 characters long. |
| `accountId` | `string` | Account ID of this floodlight activity. This is a read-only field that can be left blank. |
| `idDimensionValue` | `object` | Represents a DimensionValue resource. |
| `subaccountId` | `string` | Subaccount ID of this floodlight activity. This is a read-only field that can be left blank. |
| `defaultTags` | `array` | Dynamic floodlight tags. |
| `floodlightConfigurationId` | `string` | Floodlight configuration ID of this floodlight activity. If this field is left blank, the value will be copied over either from the activity group's floodlight configuration or from the existing activity's floodlight configuration. |
| `floodlightActivityGroupId` | `string` | Floodlight activity group ID of this floodlight activity. This is a required field. |
| `secure` | `boolean` | Whether this tag should use SSL. |
| `tagFormat` | `string` | Tag format type for the floodlight activity. If left blank, the tag format will default to HTML. |
| `sslCompliant` | `boolean` | Whether the floodlight activity is SSL-compliant. This is a read-only field, its value detected by the system from the floodlight tags. |
| `userDefinedVariableTypes` | `array` | List of the user-defined variables used by this conversion tag. These map to the "u[1-100]=" in the tags. Each of these can have a user defined type. Acceptable values are U1 to U100, inclusive.  |
| `floodlightTagType` | `string` | The type of Floodlight tag this activity will generate. This is a required field. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `floodlightActivities_get` | `SELECT` | `id, profileId` | Gets one floodlight activity by ID. |
| `floodlightActivities_list` | `SELECT` | `profileId` | Retrieves a list of floodlight activities, possibly filtered. This method supports paging. |
| `floodlightActivities_delete` | `DELETE` | `id, profileId` | Deletes an existing floodlight activity. |
| `floodlightActivities_generatetag` | `EXEC` | `profileId` | Generates a tag for a floodlight activity. |
| `floodlightActivities_insert` | `EXEC` | `profileId` | Inserts a new floodlight activity. |
| `floodlightActivities_patch` | `EXEC` | `id, profileId` | Updates an existing floodlight activity. This method supports patch semantics. |
| `floodlightActivities_update` | `EXEC` | `profileId` | Updates an existing floodlight activity. |
