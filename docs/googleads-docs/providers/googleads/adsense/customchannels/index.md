---
title: customchannels
hide_title: false
hide_table_of_contents: false
keywords:
  - customchannels
  - adsense
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
<tr><td><b>Name</b></td><td><code>customchannels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adsense.customchannels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the custom channel. Format: accounts/&#123;account&#125;/adclients/&#123;adclient&#125;/customchannels/&#123;customchannel&#125; |
| `reportingDimensionId` | `string` | Output only. Unique ID of the custom channel as used in the `CUSTOM_CHANNEL_ID` reporting dimension. |
| `active` | `boolean` | Whether the custom channel is active and collecting data. See https://support.google.com/adsense/answer/10077192. |
| `displayName` | `string` | Required. Display name of the custom channel. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_adclients_customchannels_get` | `SELECT` | `accountsId, adclientsId, customchannelsId` | Gets information about the selected custom channel. |
| `accounts_adclients_customchannels_list` | `SELECT` | `accountsId, adclientsId` | Lists all the custom channels available in an ad client. |
| `accounts_adclients_customchannels_create` | `INSERT` | `accountsId, adclientsId` | Creates a custom channel. This method can only be used by projects enabled for the [AdSense for Platforms](https://developers.google.com/adsense/platforms/) product. |
| `accounts_adclients_customchannels_delete` | `DELETE` | `accountsId, adclientsId, customchannelsId` | Deletes a custom channel. This method can only be used by projects enabled for the [AdSense for Platforms](https://developers.google.com/adsense/platforms/) product. |
| `accounts_adclients_customchannels_patch` | `EXEC` | `accountsId, adclientsId, customchannelsId` | Updates a custom channel. This method can only be used by projects enabled for the [AdSense for Platforms](https://developers.google.com/adsense/platforms/) product. |
