---
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
  - chromemanagement
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.chromemanagement.reports</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `customers_reports_countChromeDevicesReachingAutoExpirationDate` | `EXEC` | `customersId` | Generate report of the number of devices expiring in each month of the selected time frame. Devices are grouped by auto update expiration date and model. Further information can be found [here](https://support.google.com/chrome/a/answer/10564947). |
| `customers_reports_countChromeDevicesThatNeedAttention` | `EXEC` | `customersId` | Counts of ChromeOS devices that have not synced policies or have lacked user activity in the past 28 days, are out of date, or are not complaint. Further information can be found here https://support.google.com/chrome/a/answer/10564947 |
| `customers_reports_countChromeHardwareFleetDevices` | `EXEC` | `customersId` | Counts of devices with a specific hardware specification from the requested hardware type (for example model name, processor type). Further information can be found here https://support.google.com/chrome/a/answer/10564947 |
| `customers_reports_countChromeVersions` | `EXEC` | `customersId` | Generate report of installed Chrome versions. |
| `customers_reports_countInstalledApps` | `EXEC` | `customersId` | Generate report of app installations. |
| `customers_reports_findInstalledAppDevices` | `EXEC` | `customersId` | Generate report of devices that have a specified app installed. |
