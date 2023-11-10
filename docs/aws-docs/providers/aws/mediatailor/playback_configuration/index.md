---
title: playback_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - playback_configuration
  - mediatailor
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>playback_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>playback_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>playback_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediatailor.playback_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ad_decision_server_url</code></td><td><code>string</code></td><td>The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.</td></tr>
<tr><td><code>avail_suppression</code></td><td><code>object</code></td><td>The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see Ad Suppression (https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;mediatailor&#x2F;latest&#x2F;ug&#x2F;ad-behavior.html).</td></tr>
<tr><td><code>bumper</code></td><td><code>object</code></td><td>The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see Bumpers (https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;mediatailor&#x2F;latest&#x2F;ug&#x2F;bumpers.html).</td></tr>
<tr><td><code>cdn_configuration</code></td><td><code>object</code></td><td>The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.</td></tr>
<tr><td><code>configuration_aliases</code></td><td><code>undefined</code></td><td>The player parameters and aliases used as dynamic variables during session initialization. For more information, see Domain Variables. </td></tr>
<tr><td><code>dash_configuration</code></td><td><code>object</code></td><td>The configuration for DASH content.</td></tr>
<tr><td><code>live_pre_roll_configuration</code></td><td><code>object</code></td><td>The configuration for pre-roll ad insertion.</td></tr>
<tr><td><code>manifest_processing_rules</code></td><td><code>object</code></td><td>The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The identifier for the playback configuration.</td></tr>
<tr><td><code>personalization_threshold_seconds</code></td><td><code>integer</code></td><td>Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to ad replacement in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see Ad Behavior in AWS Elemental MediaTailor (https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;mediatailor&#x2F;latest&#x2F;ug&#x2F;ad-behavior.html).</td></tr>
<tr><td><code>session_initialization_endpoint_prefix</code></td><td><code>string</code></td><td>The URL that the player uses to initialize a session that uses client-side reporting.</td></tr>
<tr><td><code>hls_configuration</code></td><td><code>object</code></td><td>The configuration for HLS content.</td></tr>
<tr><td><code>playback_configuration_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the playback configuration.</td></tr>
<tr><td><code>playback_endpoint_prefix</code></td><td><code>string</code></td><td>The URL that the player accesses to get a manifest from MediaTailor. This session will use server-side reporting.</td></tr>
<tr><td><code>slate_ad_url</code></td><td><code>string</code></td><td>The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags to assign to the playback configuration.</td></tr>
<tr><td><code>transcode_profile_name</code></td><td><code>string</code></td><td>The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.</td></tr>
<tr><td><code>video_content_source_url</code></td><td><code>string</code></td><td>The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
ad_decision_server_url,
avail_suppression,
bumper,
cdn_configuration,
configuration_aliases,
dash_configuration,
live_pre_roll_configuration,
manifest_processing_rules,
name,
personalization_threshold_seconds,
session_initialization_endpoint_prefix,
hls_configuration,
playback_configuration_arn,
playback_endpoint_prefix,
slate_ad_url,
tags,
transcode_profile_name,
video_content_source_url
FROM aws.mediatailor.playback_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '<Name>'
```
