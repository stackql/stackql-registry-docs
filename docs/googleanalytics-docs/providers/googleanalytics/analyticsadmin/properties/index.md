---
title: properties
hide_title: false
hide_table_of_contents: false
keywords:
  - properties
  - analyticsadmin
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>properties</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analyticsadmin.properties</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of this property. Format: properties/&#123;property_id&#125; Example: "properties/1000" |
| `createTime` | `string` | Output only. Time when the entity was originally created. |
| `displayName` | `string` | Required. Human-readable display name for this property. The max allowed display name length is 100 UTF-16 code units. |
| `account` | `string` | Immutable. The resource name of the parent account Format: accounts/&#123;account_id&#125; Example: "accounts/123" |
| `timeZone` | `string` | Required. Reporting Time Zone, used as the day boundary for reports, regardless of where the data originates. If the time zone honors DST, Analytics will automatically adjust for the changes. NOTE: Changing the time zone only affects data going forward, and is not applied retroactively. Format: https://www.iana.org/time-zones Example: "America/Los_Angeles" |
| `industryCategory` | `string` | Industry associated with this property Example: AUTOMOTIVE, FOOD_AND_DRINK |
| `parent` | `string` | Immutable. Resource name of this property's logical parent. Note: The Property-Moving UI can be used to change the parent. Format: accounts/&#123;account&#125;, properties/&#123;property&#125; Example: "accounts/100", "properties/101" |
| `serviceLevel` | `string` | Output only. The Google Analytics service level that applies to this property. |
| `expireTime` | `string` | Output only. If set, the time at which this trashed property will be permanently deleted. If not set, then this property is not currently in the trash can and is not slated to be deleted. |
| `propertyType` | `string` | Immutable. The property type for this Property resource. When creating a property, if the type is "PROPERTY_TYPE_UNSPECIFIED", then "ORDINARY_PROPERTY" will be implied. "SUBPROPERTY" and "ROLLUP_PROPERTY" types cannot yet be created via Google Analytics Admin API. |
| `updateTime` | `string` | Output only. Time when entity payload fields were last updated. |
| `currencyCode` | `string` | The currency type used in reports involving monetary values. Format: https://en.wikipedia.org/wiki/ISO_4217 Examples: "USD", "EUR", "JPY" |
| `deleteTime` | `string` | Output only. If set, the time at which this property was trashed. If not set, then this property is not currently in the trash can. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `propertiesId` | Lookup for a single "GA4" Property. |
| `list` | `SELECT` |  | Returns child Properties under the specified parent Account. Only "GA4" properties will be returned. Properties will be excluded if the caller does not have access. Soft-deleted (ie: "trashed") properties are excluded by default. Returns an empty list if no relevant properties are found. |
| `create` | `INSERT` |  | Creates an "GA4" property with the specified location and attributes. |
| `delete` | `DELETE` | `propertiesId` | Marks target Property as soft-deleted (ie: "trashed") and returns it. This API does not have a method to restore soft-deleted properties. However, they can be restored using the Trash Can UI. If the properties are not restored before the expiration time, the Property and all child resources (eg: GoogleAdsLinks, Streams, UserLinks) will be permanently purged. https://support.google.com/analytics/answer/6154772 Returns an error if the target is not found, or is not a GA4 Property. |
| `acknowledgeUserDataCollection` | `EXEC` | `propertiesId` | Acknowledges the terms of user data collection for the specified property. This acknowledgement must be completed (either in the Google Analytics UI or via this API) before MeasurementProtocolSecret resources may be created. |
| `patch` | `EXEC` | `propertiesId` | Updates a property. |
| `updateDataRetentionSettings` | `EXEC` | `propertiesId` | Updates the singleton data retention settings for this property. |
