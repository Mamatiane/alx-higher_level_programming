{"payload":{"allShortcutsEnabled":false,"fileTree":{"0x0A-python-inheritance":{"items":[{"name":"tests","path":"0x0A-python-inheritance/tests","contentType":"directory"},{"name":"0-lookup.py","path":"0x0A-python-inheritance/0-lookup.py","contentType":"file"},{"name":"1-my_list.py","path":"0x0A-python-inheritance/1-my_list.py","contentType":"file"},{"name":"10-square.py","path":"0x0A-python-inheritance/10-square.py","contentType":"file"},{"name":"100-my_int.py","path":"0x0A-python-inheritance/100-my_int.py","contentType":"file"},{"name":"101-add_attribute.py","path":"0x0A-python-inheritance/101-add_attribute.py","contentType":"file"},{"name":"11-square.py","path":"0x0A-python-inheritance/11-square.py","contentType":"file"},{"name":"2-is_same_class.py","path":"0x0A-python-inheritance/2-is_same_class.py","contentType":"file"},{"name":"3-is_kind_of_class.py","path":"0x0A-python-inheritance/3-is_kind_of_class.py","contentType":"file"},{"name":"4-inherits_from.py","path":"0x0A-python-inheritance/4-inherits_from.py","contentType":"file"},{"name":"5-base_geometry.py","path":"0x0A-python-inheritance/5-base_geometry.py","contentType":"file"},{"name":"6-base_geometry.py","path":"0x0A-python-inheritance/6-base_geometry.py","contentType":"file"},{"name":"7-base_geometry.py","path":"0x0A-python-inheritance/7-base_geometry.py","contentType":"file"},{"name":"8-rectangle.py","path":"0x0A-python-inheritance/8-rectangle.py","contentType":"file"},{"name":"9-rectangle.py","path":"0x0A-python-inheritance/9-rectangle.py","contentType":"file"},{"name":"README.md","path":"0x0A-python-inheritance/README.md","contentType":"file"}],"totalCount":16},"":{"items":[{"name":"0x07-python-test_driven_development","path":"0x07-python-test_driven_development","contentType":"directory"},{"name":"0x0A-python-inheritance","path":"0x0A-python-inheritance","contentType":"directory"},{"name":"0x0C-python-almost_a_circle","path":"0x0C-python-almost_a_circle","contentType":"directory"},{"name":"0x17 C - Doubly linked lists","path":"0x17 C - Doubly linked lists","contentType":"directory"},{"name":"0x18 C - Dynamic libraries","path":"0x18 C - Dynamic libraries","contentType":"directory"},{"name":"100-realloc.c","path":"100-realloc.c","contentType":"file"},{"name":"101-mul.c","path":"101-mul.c","contentType":"file"},{"name":"101-password","path":"101-password","contentType":"file"},{"name":"2-calloc.c","path":"2-calloc.c","contentType":"file"},{"name":"3-array_range.c","path":"3-array_range.c","contentType":"file"},{"name":"_putchar.c","path":"_putchar.c","contentType":"file"},{"name":"main.h","path":"main.h","contentType":"file"}],"totalCount":12}},"fileTreeProcessingTime":6.98132,"foldersToFetch":[],"reducedMotionEnabled":null,"repo":{"id":627534744,"defaultBranch":"main","name":"alx","ownerLogin":"sadatmisr","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-04-13T17:04:55.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/130691074?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1695082556.0","canEdit":false,"refType":"branch","currentOid":"907071687d98b6e848fd75176358115c4081617f"},"path":"0x0A-python-inheritance/101-add_attribute.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/python3","\"\"\"Defines a function that adds attributes to objects.\"\"\"","","","def add_attribute(obj, att, value):","    \"\"\"Add a new attribute to an object if possible.","    Args:","        obj (any): The object to add an attribute to.","        att (str): The name of the attribute to add to obj.","        value (any): The value of att.","    Raises:","        TypeError: If the attribute cannot be added.","    \"\"\"","    if not hasattr(obj, \"__dict__\"):","        raise TypeError(\"can't add new attribute\")","    setattr(obj, att, value)"],"stylingDirectives":[[{"start":0,"end":18,"cssClass":"pl-c"}],[{"start":0,"end":57,"cssClass":"pl-s"}],[],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":17,"cssClass":"pl-en"},{"start":18,"end":21,"cssClass":"pl-s1"},{"start":23,"end":26,"cssClass":"pl-s1"},{"start":28,"end":33,"cssClass":"pl-s1"}],[{"start":4,"end":52,"cssClass":"pl-s"}],[{"start":0,"end":9,"cssClass":"pl-s"}],[{"start":0,"end":53,"cssClass":"pl-s"}],[{"start":0,"end":59,"cssClass":"pl-s"}],[{"start":0,"end":38,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":52,"cssClass":"pl-s"}],[{"start":0,"end":7,"cssClass":"pl-s"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-c1"},{"start":11,"end":18,"cssClass":"pl-en"},{"start":19,"end":22,"cssClass":"pl-s1"},{"start":24,"end":34,"cssClass":"pl-s"}],[{"start":8,"end":13,"cssClass":"pl-k"},{"start":14,"end":23,"cssClass":"pl-v"},{"start":24,"end":49,"cssClass":"pl-s"}],[{"start":4,"end":11,"cssClass":"pl-en"},{"start":12,"end":15,"cssClass":"pl-s1"},{"start":17,"end":20,"cssClass":"pl-s1"},{"start":22,"end":27,"cssClass":"pl-s1"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/sadatmisr/alx/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/sadatmisr/alx/security/dependabot","repoSecurityAndAnalysisPath":"/sadatmisr/alx/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"101-add_attribute.py","displayUrl":"https://github.com/sadatmisr/alx/blob/main/0x0A-python-inheritance/101-add_attribute.py?raw=true","headerInfo":{"blobSize":"521 Bytes","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"4dc92d2","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fsadatmisr%2Falx%2Fblob%2Fmain%2F0x0A-python-inheritance%2F101-add_attribute.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"16","truncatedSloc":"14"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/sadatmisr/alx/discussions/new","newIssuePath":"/sadatmisr/alx/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/sadatmisr/alx/blob/main/0x0A-python-inheritance/101-add_attribute.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/sadatmisr/alx/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/sadatmisr/alx/raw/main/0x0A-python-inheritance/101-add_attribute.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"sadatmisr","repoName":"alx","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"add_attribute","kind":"function","identStart":83,"identEnd":96,"extentStart":79,"extentEnd":520,"fullyQualifiedName":"add_attribute","identUtf16":{"start":{"lineNumber":4,"utf16Col":4},"end":{"lineNumber":4,"utf16Col":17}},"extentUtf16":{"start":{"lineNumber":4,"utf16Col":0},"end":{"lineNumber":15,"utf16Col":28}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/sadatmisr/alx/branches":{"post":"YF3L-AIRXWNFiu2tnLDt7WHBLsr0dPR-h6Yq_-tr89VEmph_2-T8UjBO2KWCMRv7TWq7RQ768tpmOPjFnip2QQ"},"/repos/preferences":{"post":"dyl8uSqfijrXKcFqfsA819E3rPsiO7b2juhDNZqLywhwHTFcht262Ed9HvWkddXHkZNqXi9YHSLTLu91rbluzg"}}},"title":"alx/0x0A-python-inheritance/101-add_attribute.py at main · sadatmisr/alx"}